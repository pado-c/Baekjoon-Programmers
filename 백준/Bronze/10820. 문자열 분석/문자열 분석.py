import sys

while True:
    l,u,n,s = 0,0,0,0 #소문자, 대문자, 숫자, 공백의 개수
    string = sys.stdin.readline().rstrip('\n')
    
    if not string: #아무것도 입력되지 않은 경우 break
        break
    
    for i in string:
        if i.islower() == True:
            l += 1
        elif i.isupper() == True:
            u += 1
        elif i.isnumeric() == True:
            n += 1
        elif i.isspace() == True:
            s += 1
    
    print(l, u, n, s)