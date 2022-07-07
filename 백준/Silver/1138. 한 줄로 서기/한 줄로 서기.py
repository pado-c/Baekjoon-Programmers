N = int(input())
li = list(map(int,input().split()))
arr = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == li[i] and arr[j] == 0:
            arr[j] = i + 1
            break
        elif arr[j] == 0:
            cnt += 1
            
print(*arr)