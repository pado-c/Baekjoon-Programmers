from collections import deque
t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    queue = deque(map(int,input().split()))
    cnt = 0

    while queue:
        maxQ = max(queue) #최댓값(가장 높은 중요도)
        FirQ = queue.popleft() #queue에서 제일 앞에 위치한 값 추출
        m -=  1

        if maxQ != FirQ:
            queue.append(FirQ) 
            if m < 0:
                m = len(queue)-1
        
        elif maxQ == FirQ:
            cnt += 1
            if m < 0:
                print(cnt)
                break