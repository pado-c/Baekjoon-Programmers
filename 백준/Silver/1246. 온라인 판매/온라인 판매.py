N,M = map(int,input().split()) #달걀 수, 고객 수
P = [int(input()) for _ in range(M)] #제시 가격

price = 0  #가격
max_profit = 0  #최대수익

P.sort()  #오름차순 정렬
for i in P:
    if (M - P.index(i)) > N :
        continue
    
    profit = i * (M - P.index(i))  #가격 * 구매가능한 손님 수
    if profit > max_profit:
        max_profit = profit
        price = i

print(price,max_profit)