def solution(num):
    if num == 1: return 0
    cnt = 0
    # num이 1이 되거나, 작업을 500번 반복할 때까지 while문 반복
    while True:
        if cnt == 500: return -1
        if num == 1: return cnt
        num = num/2 if num%2 == 0 else num*3+1
        cnt += 1