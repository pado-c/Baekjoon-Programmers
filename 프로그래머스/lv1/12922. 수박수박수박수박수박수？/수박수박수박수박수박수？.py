def solution(n):
    keyword = '수박'
    if n%2 == 0:
        answer = keyword*(n//2)
        return answer
    else:
        answer = keyword*(n//2 + 1)
        return answer[:-1]