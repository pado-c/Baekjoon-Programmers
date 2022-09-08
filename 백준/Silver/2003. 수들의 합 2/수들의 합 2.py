import sys
input = sys.stdin.readline

n, m = map(int,input().split())
num = list(map(int,input().split()))
start, end, total, cnt = 0, 0, 0, 0

while True:
  if total > m:
    total -= num[end]
    end += 1
  elif start == n:
    break
  else:
    total += num[start]
    start += 1
  
  if total == m:
    cnt += 1

print(cnt)