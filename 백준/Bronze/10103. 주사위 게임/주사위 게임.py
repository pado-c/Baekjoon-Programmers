n = int(input())
sang, chang = 100, 100

for _ in range(n):
  s, c = map(int,input().split())
  
  if s > c:
    chang -= s
  elif s < c:
    sang -= c
  else:
    continue

print(sang)
print(chang)