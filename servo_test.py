import Adafruit_PCA9685
import time

# PCA9685初期設定
pwm = Adafruit_PCA9685.PCA9685(busnum=1)
pwm.set_pwm_freq(60)


def set_angle(index, angle):
  global pwm
  pulse_min = 123 - 15
  pulse_max = 590 - 15
  pulse = (angle / 180) * (pulse_max - pulse_min) + pulse_min
  pwm.set_pwm(index, 0, pulse)


def main():
  t0 = time.time()
  while True:
    angle = 0
    print(f'{angle}')
    set_angle(0, angle)
    set_angle(2, angle)
    set_angle(4, angle)
    set_angle(6, angle)
    set_angle(8, angle)
    time.sleep(1)
    angle = 180
    print(f'{angle}')
    set_angle(0, angle)
    set_angle(2, angle)
    set_angle(4, angle)
    set_angle(6, angle)
    set_angle(8, angle)
    time.sleep(1)


if __name__ == '__main__':
  main()
