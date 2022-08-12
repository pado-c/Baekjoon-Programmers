money = 1000 - int(input()) #거슬러 받아야 할 돈
changes = [500, 100, 50, 10, 5, 1] # JOI잡화점 잔돈 종류

cnt = 0 #잔돈 개수
for c in changes:
  if c > money:
    continue
  
  i = money // c
  cnt += i
  money -= i*c

print(cnt)