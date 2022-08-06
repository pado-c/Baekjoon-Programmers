import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수
for _ in range(T):
    N, M  = map(int,input().split()) # 국가 수, 비행기 종류
    for _ in range(M):
        a, b = map(int,input().split()) #  a와 b를 왕복
    
    print(N - 1)