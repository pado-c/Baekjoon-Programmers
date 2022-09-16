import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
item = [[0, 0]]
for _ in range(N):
    item.append(list(map(int,input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < item[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], item[i][1] + dp[i-1][j - item[i][0]])

print(dp[N][K])