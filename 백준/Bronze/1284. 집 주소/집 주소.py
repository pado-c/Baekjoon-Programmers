while True:
  n = input()
  if n == "0":
    break
  
  res = len(n) + 1
  for i in n:
    if i == "1":
      res += 2
    elif i == "0":
      res += 4
    else:
      res += 3
      
  print(res)