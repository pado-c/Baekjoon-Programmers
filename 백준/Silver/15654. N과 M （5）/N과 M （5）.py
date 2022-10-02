from itertools import permutations

N, M = map(int, input().split())
numlist = sorted(list(map(int, input().split())))
pmt_numlist = list(permutations(numlist, M))

for i in pmt_numlist:
  print(*i)