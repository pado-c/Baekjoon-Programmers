t = int(input())

def calc(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return calc(num-1) + calc(num-2) + calc(num-3)
    

for i in range(t):
    num = int(input())
    print(calc(num))
