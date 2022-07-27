stack = []
res = []
count = 1
temp = True

N = int(input())

for i in range(N):
    num = int(input())
    
    while count <= num:
        stack.append(count)
        res.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        temp = False
        break
 
if temp == True:
    for i in res:
        print(i)
else:
    print('NO')