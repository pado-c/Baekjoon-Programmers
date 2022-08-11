n = int(input()) #사람 수
p = list(map(int,input().split())) #각 사람이 걸리는 시간

p.sort()
res = []

for i in range(n):
  if i == 0:
    res.append(p[i])
  else:
    res.append(res[-1] + p[i])

print(sum(res))