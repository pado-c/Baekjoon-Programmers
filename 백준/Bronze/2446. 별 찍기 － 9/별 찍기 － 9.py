n = int(input())

for i in range(n):
    space = ' ' * i
    star = '*' * ((n-i)*2 -1)
    print(space + star)
    
for j in range(n - 2, -1, -1):
    space = ' ' * j
    star = '*' * ((n-j)*2 -1)
    print(space + star)