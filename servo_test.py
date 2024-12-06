from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio

# サーボ設定
i2c = busio.I2C(SCL, SDA)
pwm = PCA9685(i2c)
pwm.frequency = 50

# サーボのパラメータ
pins = [0, 2, 4, 6, 8, 10]
mins = [124, 112, 118, 165, 89, 112]
maxs = [492, 487, 486, 520, 468, 489]


def set_angle(id, angle):
  """
    サーボの角度を設定する関数
    :param id: サーボID (0〜5)
    :param angle: 設定する角度 (0〜180度)
    """
  pulse = int((angle / 180) * (maxs[id] - mins[id]) + mins[id])
  pwm.channels[pins[id]].duty_cycle = pulse


# メイン処理
if __name__ == "__main__":
  try:
    # 例: サーボ0を90度に設定
    set_angle(0, 90)
    print("Servo 0 set to 90 degrees")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    pwm.deinit()  # リソースの解放
