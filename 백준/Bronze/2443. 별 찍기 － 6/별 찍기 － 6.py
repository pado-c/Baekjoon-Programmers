n = int(input())

for i in range(n, 0, -1):
  star = "*" * (2*i-1)
  space = " " * (n - i)
  print(space + star)