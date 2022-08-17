x = int(input())
n = int(input())
for _ in range(n):
  price, cnt = map(int,input().split())
  x -= price * cnt

if x == 0:
  print("Yes")
else:
  print("No")