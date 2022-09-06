x_dict = {}
y_dict = {}

for _ in range(3):
  x, y = map(int,input().split())
  if x in x_dict:
    x_dict[x] += 1
  else:
    x_dict[x] = 1
  
  if y in y_dict:
    y_dict[y] += 1
  else:
    y_dict[y] = 1

for k, v in x_dict.items():
  if v == 1:
    print(k, end=' ')

for k, v in y_dict.items():
  if v == 1:
    print(k)
