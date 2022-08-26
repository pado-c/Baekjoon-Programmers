while True:
    member = input().split()
    if member == ['#', '0', '0']: break
    
    if int(member[1]) > 17 or int(member[2]) >= 80:
        res = member[0] + ' Senior'
    else:
        res = member[0] + ' Junior'
    
    print(res)