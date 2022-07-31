import sys
N, M = map(int,sys.stdin.readline().split())
#저장된 사이트 수, 찾으려는 사이트 수
site = {}

for _ in range(N):
    url, Password = sys.stdin.readline().split()
    site[url] = Password

for _ in range(M):
    findPassword = sys.stdin.readline().rstrip()
    print(site[findPassword])