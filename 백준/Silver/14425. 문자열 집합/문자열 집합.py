n, m = map(int,input().split())
str = []
cnt = 0

for _ in range(n):
  str.append(input())
  
for _ in range(m):
  s = input()
  if s in str:
    cnt += 1

print(cnt)