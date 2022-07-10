N = int(input())
result = 0

while N >= 0:
    if N % 5 == 0:  # 5으로 나눠떨어질 때
        result += N//5
        print(result)
        break

    N -= 3
    result += 1
    
    if N == 1 or N == 2:  # 조합이 불가할 때
        print(-1)
        break
    
    if N == 0:  # 3으로 나눠떨어질 때
        print(result)
        break