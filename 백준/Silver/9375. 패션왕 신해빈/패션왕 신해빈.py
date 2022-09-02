from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    wear = []
    for _ in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1 

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)