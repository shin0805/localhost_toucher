import requests
import pigpio
import time

SERVO_PIN = 18
pi = pigpio.pi()


def fetch_localhost_content():
  url = "http://192.168.10.105:8081"
  try:
    response = requests.get(url)
    response.raise_for_status()  # HTTPエラーがあれば例外を発生
    return response.text
  except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
    return "NONE"


def extract_numbers(input_string):
  # Split the string by colon (":") and comma (",") to isolate the numbers
  parts = input_string.split(":")[-1].split(",")
  # Strip whitespace and convert the parts to integers
  numbers = [int(part.strip()) for part in parts if part.strip().isdigit()]
  # Take the last 5 numbers and return them
  return numbers[-5:]


def set_angle(angle):
  assert 46 <= angle <= 130, '角度は46から130の間でなければなりません'
  pulse_width = (angle / 180) * (2500 - 500) + 500
  pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)


def map_to_range(value, src_min, src_max, dst_min, dst_max):
  return dst_min + (value - src_min) * (dst_max - dst_min) / (src_max - src_min)


if __name__ == "__main__":
  while True:
    text = fetch_localhost_content()
    nums = extract_numbers(text)
    angles = [map_to_range(num, 0, 3000, 46, 130) for num in nums]
    set_angle(angles[0])
    # print(nums)
    print(f"angles: {angles}, touchdesigner: {nums}")
    time.sleep(0.05)
