import sys
n , m = map(int, sys.stdin.readline().split())
nums = []

def dfs(d):
  if d == m:
    print(*nums)
    return
  
  for i in range(1, n+1):
    nums.append(i)
    dfs(d+1)
    nums.pop()
    
dfs(0)