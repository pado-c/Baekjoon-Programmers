import sys
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편으로
# 런타임 에러에 걸리지 않기 위해 사용!
sys.setrecursionlimit(100000)
input = sys.stdin.readline

t = int(input()) #test case

def dfs(x, y):
  if [x, y] in graph:
    graph.remove([x,y])
    
    dfs(x, y+1)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x-1, y)

for _ in range(t):
  m, n, k = map(int,input().split())
  graph = [list(map(int,input().split())) for _ in range(k)]
  
  cnt = 0
  
  while(graph):
    cnt += 1
    dfs(graph[0][0], graph[0][1])
  
  print(cnt)