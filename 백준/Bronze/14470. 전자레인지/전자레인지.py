A = int(input()) #원래의 고기 온도
B = int(input()) #목표 온도
C = int(input()) #데우는 데 걸리는 시간
D = int(input()) #해동하는 데 걸리는 시간
E = int(input()) #얼어있지 않은 고기를 데우는 데 걸리는 시간
time = 0

if A < 0:
  time += abs(A) * C
  A = 0

if A <= 0:
  time += D

time += (B - A) * E

print(time)