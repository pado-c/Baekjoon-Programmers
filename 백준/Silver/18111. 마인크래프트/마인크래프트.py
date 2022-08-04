import sys
input = sys.stdin.readline

N, M, B = map(int,input().split()) #세로, 가로, 가진 블록
block = [list(map(int,input().split())) for _ in range(N)]

ans = sys.maxsize # int의 최대 정수값
height = 0

for h in range(257): #땅의 높이는 256을 초과할 수 없음
    add_block = 0 #주머니에서 꺼내서 쌓음 (1s)
    erase_block = 0 #제거해서 주머니에 넣음 (2s)
    for i in range(N):
        for j in range(M):
            # block[i][j]의 높이가 h보다 작은 경우, 블럭을 꺼내 쌓음
            if block[i][j] < h:
                add_block += h - block[i][j]
            # block[i][j]의 높이가 h와 같거나 큰 경우, 제거해 주머니에 넣음
            else:
                erase_block += block[i][j] - h
    
    # 사용할 수 있는 블럭보다 필요한 블럭이 많은 경우
    if B + erase_block < add_block:
        continue
    
    time = 2 * erase_block + add_block
    if time <= ans:
        ans = time
        height = h

print(ans, height)