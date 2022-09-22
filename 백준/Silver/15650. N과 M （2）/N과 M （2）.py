from itertools import combinations

n, m = map(int,input().split())

num = [i for i in range(1, n+1)]
array = list(combinations(num, m))

for i in array:
  print(*i)