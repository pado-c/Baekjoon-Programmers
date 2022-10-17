n = int(input())
grading = list(map(int,input().split()))
correct = 0
score = 0
for i in grading:
  if i == 1:
    correct+=1
    score+=correct
  else:
    correct = 0

print(score)