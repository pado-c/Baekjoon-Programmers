k, n = map(int,input().split()) # 이미 가지고 있는 랜선의 수 k, 필요한 랜선의 수 n
list = [int(input()) for _ in range(k)]

#이분탐색
start, end = 1, max(list)
while start <= end: 
    mid = (start + end) // 2
    lineNum = 0 # 자른 랜선 수
    for i in list:
        lineNum += i // mid
    
    if lineNum >= n: # 자른 랜선 수가 필요한 랜선 수보다 많거나 같은 경우
        start = mid + 1
    else:
        end = mid - 1

print(end)