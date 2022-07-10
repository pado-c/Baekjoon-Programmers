l = int(input())
li = list(map(int,input().split()))
n = int(input())

a = 0
b = 0
result = 0
li.sort()   #정렬

for i in range(l):
    if n < li[i]:
        a = li[i - 1] #시작점 계산 기준
        b = li[i]   #끝점 계산 기준
        break
        
if n < li[0]:   #li[0]보다 n이 작을 때
    for i in range(1, n+1):
        for j in range(n, li[0]):
            if i == j:
                continue
            else:
                result += 1

else:   #li[0]보다 n이 클 때
    for i in range(a+1, n+1):  #시작점
        for j in range(n, b):  #끝점
            if i == j:
                continue
            result += 1

print(result)