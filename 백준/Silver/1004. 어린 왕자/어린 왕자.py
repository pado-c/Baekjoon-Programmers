import math
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  x1, y1, x2, y2 = map(int,input().split())
  n = int(input())
  cnt = 0
  
  for _ in range(n):
    cx, cy, r = map(int,input().split())
    # math.sqrt() 메서드는 숫자의 제곱근 반환
    dist_1 = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
    dist_2 = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)
    if (dist_1 > r and dist_2 < r) or (dist_1 < r and dist_2 > r):
      cnt += 1
    
  print(cnt)