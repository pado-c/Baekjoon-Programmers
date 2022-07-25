n, m = map(int,input().split())

A, B = [], []
for _ in range(n):
    A += list(map(int,input().split()))
for _ in range(n):
    B += list(map(int,input().split()))

for _ in range(n):
    res = []
    for i in range(0,n*m,m):
        for j in range(m):
            res += [A[i+j] + B[i+j]]

for i in range(len(res)):
    if (i+1) % m == 0:
        print(res[i])
    else:
        print(res[i],end = ' ')