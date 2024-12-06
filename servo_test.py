import Adafruit_PCA9685
import time

# PCA9685初期設定
pwm = Adafruit_PCA9685.PCA9685(busnum=1)
pwm.set_pwm_freq(60)


def main():
  t0 = time.time()
  while True:
    palse = int((time.time() - t0) % 10 * 100)
    palse = 123 - 40
    print(f'{palse}')
    pwm.set_pwm(0, 0, palse)
    time.sleep(1)
    palse = 590 - 40
    print(f'{palse}')
    pwm.set_pwm(0, 0, palse)
    time.sleep(1)


if __name__ == '__main__':
  main()
