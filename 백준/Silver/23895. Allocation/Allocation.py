cnt = 0
t = int(input())

for _ in range(t):
    n, b = map(int,input().split())
    price = sorted(list(map(int,input().split())))
    buy = 0
    cnt += 1
    
    for i in price:
        if b >= i:
            b -= i
            buy += 1
        
    print(f"Case #{cnt}: {buy}")
    price.clear()