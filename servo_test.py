import Adafruit_PCA9685
import time

# PCA9685初期設定
pwm = Adafruit_PCA9685.PCA9685(busnum=1)
pwm.set_pwm_freq(60)


def main():
  while True:
    print('0')
    pwm.set_pwm(0, 0, 0)
    time.sleep(1)
    print('100')
    pwm.set_pwm(0, 0, 100)
    time.sleep(1)
    print('200')
    pwm.set_pwm(0, 0, 200)
    time.sleep(1)


if __name__ == '__main__':
  main()
