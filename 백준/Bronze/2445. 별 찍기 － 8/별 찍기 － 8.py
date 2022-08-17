n = int(input())

for i in range(1, n+1):
  star = "*" * i
  space = " " * (2*n - i*2)
  print(star + space + star)

for i in range(n-1, 0, -1):
  star = "*" * i
  space = " " * (2*n - i*2)
  print(star + space + star)
