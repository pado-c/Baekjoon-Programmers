N = int(input())
list = {}
cnt = 0

for _ in range(N):
    inputed = input()
    
    if inputed == "ENTER":
        cnt += len(list)
        list = {} 
        
    else:
        if inputed not in list:
            list[inputed] = 1
        
cnt += len(list)
print(cnt)