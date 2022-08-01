import sys

input = sys.stdin.readline
N, M, V = map(int,input().split())

# 인접행렬(adjacency matrix)
# 그래프에서 어느 노드들끼리 연결되었는지 나타내는 이차원 행렬
graph = [[0] * (N+1) for _ in range(N+1)]
# 방문 리스트
visit = [0] * (N+1)

for _ in range(M):
    x, y =list(map(int,input().split()))
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(V):
    visit[V] = 1
    print(V, end = " ")
    for i in range(1, N+1):
        if visit[i] == 0 and graph[V][i] == 1: # 해당 정점에 연결된 정점이면서 아직 방문을 안했으면
            dfs(i)
    
def bfs(V):
    queue = [V] # 현재 방문중인 정점를 큐에 넣는다
    visit[V] = 0
    while queue:
        V = queue.pop(0) # 방문한 정점 제거
        print(V, end = " ") # 정점 제거하면서 출력
        for i in range(1, N+1):
            if visit[i] == 1 and graph[V][i] == 1: # 해당 정점에 연결된 정점이면서 아직 방문을 안했으면
                queue.append(i) # 정점을 큐에 넣는다
                visit[i] = 0

dfs(V)
print()
bfs(V)