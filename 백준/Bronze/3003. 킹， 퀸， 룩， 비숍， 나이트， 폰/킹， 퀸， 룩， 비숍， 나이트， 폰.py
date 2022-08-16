nums = list(map(int,input().split()))
chess = [1,1,2,2,2,8]
res = []

for i in range(6):
  n = chess[i] - nums[i]
  res.append(n)

print(*res)