import time

start = time.time()
while True:
  print(f'{((time.time() - start) % 2)}')
