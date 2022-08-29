#에라토스테네스의 체
n = 123456*2 + 1
N = [True] * n
for i in range(2, int(n**0.5) + 1):
  if N[i]:
    for j in range(2*i, n, i):
      N[j] = False

while True:
  num = int(input())
  if num == 0:
    break
  cnt = 0
  for i in range(num+1, 2*num + 1):
    if N[i]:
      cnt += 1
  print(cnt)