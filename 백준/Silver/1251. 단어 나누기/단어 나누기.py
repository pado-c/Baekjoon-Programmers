word = list(input())
res = []

for i in range(1, len(word) - 1):
  for j in range(i+1, len(word)):
    first = word[:i]
    second = word[i:j]
    third = word[j:]
    
    first.reverse()
    second.reverse()
    third.reverse()
    
    res.append("".join(first + second + third))

res.sort()
print(res[0])