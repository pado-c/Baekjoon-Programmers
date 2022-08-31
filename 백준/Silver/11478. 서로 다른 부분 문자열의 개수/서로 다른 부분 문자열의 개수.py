li = set()
str = input().rstrip()
for i in range(len(str)):
  for j in range(i, len(str)):
    li.add(str[i:j+1])

print(len(li))