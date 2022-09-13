scenario = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    scenario += 1
    student = [input() for _ in range(n)]
    
    dict = {}
    for _ in range(n*2 - 1):
        a, b = input().split()
        if int(a) in dict:
            dict[int(a)] -= 1
        else:
            dict[int(a)] = 1
    
    for k, v in dict.items():
        if v == 1:
            print(scenario, student[k-1])