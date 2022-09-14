def solution(a, b):
    if a == b:
        return a
    else:
        answer = 0
        min_max = sorted([a,b])
        for i in range(min_max[0], min_max[1] + 1):
            answer += i
        return answer