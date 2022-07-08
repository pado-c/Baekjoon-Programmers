while True:
    num = input()
    if num == '0':
        break
    check = ''
    for i in range(len(num)):
        if num[i] == num[-i-1]:
            check+=num[i]
        else:
            continue
    if check == num:
        print('yes')
    else:
        print('no')