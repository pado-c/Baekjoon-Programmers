import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
stars = [[" " for _ in range(n)] for _ in range(n)]

def draw(size, x, y):
  if size == 1:
    stars[x][y] = "*"
    
  else:
    n_size = size // 3
    for dx in range(3):
      for dy in range(3):
        if dx != 1 or dy != 1:
          draw(n_size, dx*n_size + x, dy*n_size + y)
  

draw(n, 0, 0)
for i in stars:
  print(''.join(i))