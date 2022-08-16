from collections import deque
import sys
input = sys.stdin.readline

#상하좌우 비교를 위해
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = cnt
    while queue:
        x, y = queue.popleft() # 가장 앞에 있는 좌표 추출
        for i in range(4):
            now_x = x + dx[i]
            now_y = y + dy[i]
            if 0 <= now_x < n and 0 <= now_y < n and graph[now_x][now_y] == graph[x][y] and visited[now_x][now_y] == 0:
              # 좌표의 시작, 끝이 0, n-1 이므로 0보다 크거나 같고, n보다 작아야 함 && 구역이 같아야 하고 && 방문기록이 없어야 함
                    queue.append([now_x, now_y])
                    visited[now_x][now_y] = 1

n = int(input())
graph = [list(map(str,input())) for _ in range(n)]
queue = deque()

# 적록색약이 아닌 사람이 봤을 때 구역의 수 구하기
cnt = 0 #구역의 수
visited = [[0]*n for _ in range(n)] #방문기록
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

# 적록색약인 사람이 봤을 때 구역의 수 구하기
# 모든 R을 G로 통일
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

cnt = 0 #구역의 수 초기화
visited = [[0]*n for _ in range(n)] #방문기록 초기화
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)