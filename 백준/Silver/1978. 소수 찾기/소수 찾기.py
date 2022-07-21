n = int(input())
numbers = list(map(int,input().split())) 
prime = 0  #소수인 수의 개수

for i in numbers:
    cnt = 0
    if i == 1:  #1은 소수가 아님
        continue
    
    for j in range(2,i): #1과 자기자신을 제외한 수로 나누어지면
        if i % j == 0:   #소수가 아님
            cnt += 1
    if cnt == 0:
        prime += 1
        
print(prime)