person = 0
li = []
for _ in range(4):
  off, on = map(int,input().split())
  person = person - off + on
  li.append(person)
print(max(li))