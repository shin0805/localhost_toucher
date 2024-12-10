import requests
import pigpio
import time
import Adafruit_PCA9685

SERVO_PIN = 18
pi = pigpio.pi()
# PCA9685初期設定
pwm = Adafruit_PCA9685.PCA9685(busnum=1)
pwm.set_pwm_freq(60)


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
  # Take the last 6 numbers and return them
  return numbers[-6:]


def set_angle(index, angle, for_switch=False):
  global pwm
  if not for_switch:
    pulse_min = 123 - 15
    pulse_max = 590 - 15
    pulse = int((angle / 180) * (pulse_max - pulse_min) + pulse_min)
    # pwm.set_pwm(index, 0, pulse)
  else:
    pulse_min = 123
    pulse_max = 614
    pulse = int((angle / 180) * (pulse_max - pulse_min) + pulse_min)
    # pwm.set_pwm(index, 0, pulse)


def map_to_range(value, src_min, src_max, dst_min, dst_max):
  mapped_value = dst_min + (value - src_min) * (dst_max - dst_min) / (src_max - src_min)
  return max(dst_min, min(mapped_value, dst_max))


if __name__ == "__main__":
  start_time = time.time()
  pre_switch = False
  # パラメータ
  SWITCH_OFF_ANGLE = 0  # スイッチオフの角度 (deg)
  SWITCH_ON_ANGLE = 30  # スイッチオンの角度 (deg)
  SWITCH_CYCLE_TIME = 2  # スイッチの動作周期時間 (sec) (整数)
  SWITCH_ON_TIME = 0.5  # スイッチオンのための時間 (sec) (動作周期時間よりは短く)

  set_angle(10, SWITCH_OFF_ANGLE)
  try:
    while True:
      now_time = time.time() - start_time
      text = fetch_localhost_content()
      nums = extract_numbers(text)
      angles = [0, 0, 0, 0, 0, 0]
      angles[0] = map_to_range(nums[0], 0, 6000, 46, 130)  # touch designerのMIN, MAX, サーボのMIN, MAX
      angles[1] = map_to_range(nums[1], 0, 6000, 46, 130)
      angles[2] = map_to_range(nums[2], 0, 6000, 46, 130)
      angles[3] = map_to_range(nums[3], 0, 6000, 46, 130)
      angles[4] = map_to_range(nums[4], 0, 6000, 46, 130)
      for i in range(5):
        set_angle(i * 2, angles[i])
      if (not pre_switch) and (nums[5] == 1):  # 立ち上がりに反応
        pre_switch = True
        swich_time = now_time
      elif nums[5] == 0:
        pre_switch = False
      if pre_switch:
        if (now_time - swich_time) % int(SWITCH_CYCLE_TIME) <= SWITCH_ON_TIME:
          set_angle(10, SWITCH_ON_ANGLE)
          angles[5] = SWITCH_ON_ANGLE
        else:
          set_angle(10, SWITCH_OFF_ANGLE)
          angles[5] = SWITCH_OFF_ANGLE
      print(f"angles: {angles}, touchdesigner: {nums}")
      time.sleep(0.05)
  except Exception as e:
    print("------------ Finished! ---------------")
    for i in range(5):
      set_angle(i * 2, 55)
    set_angle(10, SWITCH_OFF_ANGLE)
  finally:
    print("------------ Finished! ---------------")
    for i in range(5):
      set_angle(i * 2, 55)
