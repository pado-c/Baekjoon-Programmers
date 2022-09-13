import math

t = int(input())
for _ in range(t):
    res = 0
    num = list(map(int,input().split()))
    for i in range(1, num[0]):
        for j in range(i+1, num[0]+1):
            gcd = math.gcd(num[i], num[j])
            res += gcd
    print(res)