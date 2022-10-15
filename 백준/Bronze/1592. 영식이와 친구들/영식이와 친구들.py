n, m, l = map(int,input().split())
passCnt = 0  # 공을 던진 횟수
cnt = 1      # 1번이 공을 받은 횟수
ball = 1     # 공을 받은 사람

while cnt < m:
  ball = (ball + l)%n
  if ball == 1:
    cnt += 1
  
  passCnt += 1

print(passCnt)