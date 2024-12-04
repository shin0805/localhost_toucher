import requests
import time


def fetch_localhost_content():
  url = "http://192.168.10.105:8081"
  try:
    response = requests.get(url)
    response.raise_for_status()  # HTTPエラーがあれば例外を発生
    # print("HTTP Status Code:", response.status_code)
    # print("Content:")
    print(response.text)
  except requests.exceptions.RequestException as e:
    print("An error occurred:", e)


if __name__ == "__main__":
  while True:
    fetch_localhost_content()
    time.sleep(0.05)
