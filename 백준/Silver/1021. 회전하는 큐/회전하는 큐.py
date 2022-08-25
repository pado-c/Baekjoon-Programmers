from collections import deque

n, m = map(int,input().split()) # 큐의 크기 n, 뽑아내려고 하는 수의 개수 m
idx = list(map(int,input().split())) # 뽑아내려고 하는 수의 위치
deq = deque([i for i in range(1,n+1)]) # n이 10이라면,  [1,2, ..., 10]
cnt = 0

for i in idx:
  while True:
    if deq[0] == i: #deq의 첫 번째 원소가 i인 경우, i를 뽑아내고 다음 idx로 넘어감
      deq.popleft()
      break
      
    else: #deq의 첫 번째 원소 i가 아닌 경우
      if deq.index(i) <= len(deq)//2: #왼쪽으로 이동하는 게 더 빠른 경우
        deq.rotate(-1) #왼쪽으로 한 칸 이동
      else:
        deq.rotate(1) #오른쪽으로 한 칸 이동
      
      cnt += 1
  
print(cnt)