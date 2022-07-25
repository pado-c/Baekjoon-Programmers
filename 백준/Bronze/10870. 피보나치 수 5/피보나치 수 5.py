def calc(n):
    if n <= 1:
        return n
    return calc(n-1) + calc(n-2)

n = int(input())
print(calc(n))
