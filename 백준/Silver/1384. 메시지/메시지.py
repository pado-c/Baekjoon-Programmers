group = 0

while True:
  n = int(input())
  if n == 0:break
  
  group += 1
  dict = {}
  member = []
  for _ in range(n):
    paper = input().split()
    name, nasty = paper[0], paper[1:]
    member.append(name)
    temp = [i for i in range(n-1) if nasty[i] == "N"]
    if temp: dict[name] = temp
    
  print(f"Group {group}")
  if dict:
    for k, v in dict.items():
      for idx in v:
        print(f"{member[member.index(k) - (idx + 1)]} was nasty about {k}")
  else:
    print("Nobody was nasty")
  
  print()