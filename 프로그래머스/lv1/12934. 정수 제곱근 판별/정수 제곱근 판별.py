def solution(n):
    num = n ** (1/2)
    if str(num)[-2:] == ".0":
        num += 1
        return num ** 2
    else: 
        return -1
    