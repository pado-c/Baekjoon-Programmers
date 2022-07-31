import sys

input = sys.stdin.readline
N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
res = [0,0]

def blockColorChcker(x, y, N) :
    color = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] :
                blockColorChcker(x, y, N//2)
                blockColorChcker(x, y+N//2, N//2)
                blockColorChcker(x+N//2, y, N//2)
                blockColorChcker(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        res[0] += 1
    else:
        res[1] += 1
    
blockColorChcker(0,0,N)
for i in res:
    print(i)