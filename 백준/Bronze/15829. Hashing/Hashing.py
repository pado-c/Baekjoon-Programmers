M = 1234567891
r = 31
L = int(input()) #입력될 문자열 길이
InputStr = input()

res = 0

for i in range(L):
    num = ord(InputStr[i]) - 96 #a의 아스키코드는 97...
    res += num * (r ** i)
    
print(res % M)