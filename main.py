import requests
import time


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


if __name__ == "__main__":
  while True:
    text = fetch_localhost_content()
    nums = extract_numbers(text)
    print(nums)
    time.sleep(0.05)
