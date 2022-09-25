import sys
input = sys.stdin.readline

for _ in range(3):
  n = int(input())
  nums = sum([int(input()) for _ in range(n)])
  if nums > 0: print('+')
  elif nums < 0: print('-')
  else: print('0')