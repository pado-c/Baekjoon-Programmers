import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

prime = []

for i in range(m, n+1):
    checker = 0
    if i == 1:
        continue
    
    for j in range(2, i):
        if i%j == 0:
            checker += 1
            break
    if checker == 0:
        prime += [i]

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)