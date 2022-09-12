t = int(input())
num = 0

for _ in range(t):
    num += 1
    n = int(input())
    h = list(map(int,input().split()))
    
    peak = 0
    for i in range(1, n-1):
        if h[i-1] < h[i] > h[i+1]:
            peak += 1
    print("Case #{}: {}".format(num, peak))