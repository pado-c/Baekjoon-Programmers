import sys
N = int(sys.stdin.readline()) #수의 개수 입력
res = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    res[num] += 1   #num이 1번 나오면 res[num]은 1 / 2번 나오면 2.

for i in range(10001):
    if res[i] !=0:  #res에 1이 추가되어 있는 자리만 출력
        for _ in range (res[i]):
            print(i)