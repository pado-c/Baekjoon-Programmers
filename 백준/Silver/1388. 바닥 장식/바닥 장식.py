N,M = map(int,input().split())
floor = [input() for _ in range(N)]
cnt = 0

for n in range(N):  #"-"의 개수
    i = 0 
    while i < M:
        if floor[n][i] == "|":  #"|"가 나오면 i+1(열바꿈)
            i += 1
        elif floor[n][i] == "-":
            cnt += 1
            while i < M and floor[n][i] == "-": 
                #같은 행에 "-"가 인접해 있다면 i + 1
                i += 1

for m in range(M): #"|"의 개수
    i = 0
    while i < N:
        if floor[i][m] == "-":  #"-"가 나오면 i+1(행바꿈)
            i += 1
        elif floor[i][m] == "|":
            cnt += 1
            while i < N and floor[i][m] == "|":
                #같은 열에 "|"가 인접해 있다면 i + 1
                i += 1

print(cnt)