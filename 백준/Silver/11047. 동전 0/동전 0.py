import sys
input = sys.stdin.readline

n, k = map(int,input().split()) #동전 종류 n, 가치의 합 k
coins = []
for _ in range(n):
  coins.insert(0, int(input())) #입력받음과 동시에 내림차순으로 정렬

cnt = 0 #필요 동전 개수
for coin in coins:
  if coin > k: # k보다 coin의 값이 크면
    continue
  else: #크거나 같으면
    num = k//coin
    k -= coin * num
    cnt += num

print(cnt)