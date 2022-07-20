from collections import deque

n,k = map(int,input().split())
num = deque(list(map(lambda x: x, range(1,n+1)))) #1부터 n까지 수를 가진 덱 생성

print("<", end='')
while len(num) != 0:
    for i in range(k-1):
        num.append(num.popleft())
    print(num.popleft(),end = '')
    if len(num) != 0:
        print(', ',end = '')
print(">")
