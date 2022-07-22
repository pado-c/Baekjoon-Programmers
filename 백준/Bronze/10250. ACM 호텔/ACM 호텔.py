t = int(input()) #케이스 수
for _ in range(t):
    h,w,n = map(int,input().split()) #층 수, 각 층의 방 수, 손님 순서
    floor = n%h #층
    room = n//h + 1 #방
    if floor == 0: #n이 h의 배수인 경우
        floor = h
        room = n//h
    
    print(f'{floor*100 + room}')