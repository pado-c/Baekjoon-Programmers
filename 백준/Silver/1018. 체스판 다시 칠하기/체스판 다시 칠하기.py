N, M =map(int,input().split()) #세로, 가로
chess = [] #체스판 입력
for _ in range(N):
    chess += [input()]

cnt = []  #결과
for i in range(N-7):
    for j in range (M-7):
        change_to_white = 0
        change_to_black = 0
        for x in range (i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 == 0:
                    if chess[x][y] != 'W':
                        change_to_white += 1
                    if chess[x][y] != 'B':
                        change_to_black += 1
                else:
                    if chess[x][y] != 'B':
                        change_to_white += 1
                    if chess[x][y] != 'W':
                        change_to_black += 1
        cnt += [change_to_white]
        cnt += [change_to_black]

print(min(cnt))