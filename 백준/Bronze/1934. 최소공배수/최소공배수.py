import math
T = int(input())
for _ in range (T):
    a,b = map(int,input().split())
    print(math.lcm(a,b))  #a,b의 최소 공배수 출력