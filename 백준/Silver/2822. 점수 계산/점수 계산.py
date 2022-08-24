score = []
dict = {}

for i in range(8):
  s = int(input())
  score.append(s)
  dict[i] = s

score.sort(reverse=True)
total_score = score[0:5]

find_key = []
for i in total_score:
 for k, v in dict.items():
   if v == i:
     find_key.append(k+1)
find_key.sort()

print(sum(total_score))
print(*find_key)