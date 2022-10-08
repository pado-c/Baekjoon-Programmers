n = int(input())
seat = list(map(int,input().split()))
pc = [0] * 101
res = 0

for i in seat:
  if pc[i] == 0:
    pc[i] = 1
  else:
    res += 1

print(res)