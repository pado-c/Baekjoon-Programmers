H,M,S = map(int,input().split())   #시,분,초
time = int(input())   #걸리는 시간
S = time + S
M = M + S//60
H = H + M//60

print(H%24,M%60,S%60)