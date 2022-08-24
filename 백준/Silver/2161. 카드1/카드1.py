from collections import deque

n = int(input())
deq = deque(list(map(lambda x: x, range(1,n+1))))
res = deque([])

while True:
  if len(deq) == 1: #마지막 남은 카드
    res.append(deq.popleft())
    break
    
  res.append(deq.popleft()) #카드 버리기
  
  deq.rotate(-1) #카드 옮기기

print(*res)