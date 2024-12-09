import requests
import pigpio
import time

SERVO_PIN = 18
pi = pigpio.pi()


def fetch_localhost_content():
  url = "http://192.168.11.102:8081"
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
  mapped_value = dst_min + (value - src_min) * (dst_max - dst_min) / (src_max - src_min)
  return max(dst_min, min(mapped_value, dst_max))


if __name__ == "__main__":
  while True:
    text = fetch_localhost_content()
    nums = extract_numbers(text)
    angles = [0, 0, 0, 0, 0]
    angles[0] = map_to_range(nums[0], 0, 6000, 46, 130)
    angles[1] = map_to_range(nums[1], 0, 6000, 46, 130)
    angles[2] = map_to_range(nums[2], 0, 6000, 46, 130)
    angles[3] = map_to_range(nums[3], 0, 6000, 46, 130)
    angles[4] = map_to_range(nums[4], 0, 6000, 46, 130)
    # set_angle(angles[2])
    print(f"angles: {angles}, touchdesigner: {nums}")
    time.sleep(0.05)
