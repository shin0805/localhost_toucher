import time

start = time.time()
while True:
  print(f'{int((time.time() - start) % 10 * 100)}')
