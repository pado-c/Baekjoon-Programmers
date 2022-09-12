def solution(n):
    answer = n
    for i in range(2, n):
        num = n % i
        if num == 1 and answer > i:
            answer = i
    return answer