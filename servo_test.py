import Adafruit_PCA9685
import time

# PCA9685初期設定
pwm = Adafruit_PCA9685.PCA9685(busnum=1)
pwm.set_pwm_freq(60)


def main():
  while True:
    print('0')
    # pwm.set_pwm(0, 0, 100)
    pwm.set_pwm(0, 0, int((0 / 180) * (2500 - 500) + 500))
    time.sleep(1)
    # print('100')
    # pwm.set_pwm(0, 0, 100)
    print('45')
    pwm.set_pwm(0, 0, int((45 / 180) * (2500 - 500) + 500))
    time.sleep(1)
    # print('200')
    # pwm.set_pwm(0, 0, 200)
    print('90')
    pwm.set_pwm(0, 0, int((90 / 180) * (2500 - 500) + 500))
    time.sleep(1)
    # print('300')
    # pwm.set_pwm(0, 0, 300)
    print('135')
    pwm.set_pwm(0, 0, int((135 / 180) * (2500 - 500) + 500))
    time.sleep(1)
    # print('400')
    # pwm.set_pwm(0, 0, 400)
    print('180')
    pwm.set_pwm(0, 0, int((180 / 180) * (2500 - 500) + 500))
    time.sleep(1)


if __name__ == '__main__':
  main()
