import sys

def dfs(x,y) :
    #구역을 벗어났거나 이미 방문한 경우
    if x <= -1 or x >= N or y <= -1 or y >= N or visit[x][y] == 1:
        return
    
    if graph[x][y] == -1 :
        visit[x][y] = True
        return

    visit[x][y] = True

    dfs(x+graph[x][y], y)
    dfs(x, y+graph[x][y])

N=int(sys.stdin.readline())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

visit=[[False]*N for _ in range(N)]

dfs(0,0)
if visit[-1][-1] == True :
    print('HaruHaru')
else :
    print('Hing')
