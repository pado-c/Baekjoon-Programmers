t = int(input())
for _ in range(t):
  num_list = sorted(list(map(int,input().split())))
  print(num_list[-3])