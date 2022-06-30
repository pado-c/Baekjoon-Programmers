N = int(input())
score = list(map(int,input().split()))
M = max(score)
I = 0
for i in score:
  i = (i/M)*100
  I += i
print(I/N)