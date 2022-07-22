t = int(input())
for _ in range(t):
    k = int(input()) #floor
    n = int(input()) #room
    floor = list(map(lambda x: x, range(1,n+1))) #0층 [1,2,3 ...]

    for i in range(k):
        for j in range(1,n):
            floor[j] += floor[j-1]

    print(floor[-1])