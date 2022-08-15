import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

only_mone = 0
only_one = 0
only_zero = 0

def cut(x,y,n):
  global only_mone, only_zero, only_one
  
  check = graph[x][y]
  for i in range(x,x+n):
    for j in range(y, y+n):
      if check != graph[i][j]:
        for a in range(3):
          for b in range(3):
            cut(x + a*n//3, y + b*n//3, n//3)
        return
  
  if check == 1:
    only_one += 1
  elif check == -1:
    only_mone += 1
  else:
    only_zero += 1
  
  
cut(0,0,n)
print(only_mone)
print(only_zero)
print(only_one)