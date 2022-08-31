import itertools

n, m = map(int,input().split())

# n = 3 이라면 num_li = [1,2,3]
num_li = list(map(lambda x: x, range(1, n+1)))
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
res = itertools.permutations(num_li, m)

for r in res:
  print(*r)