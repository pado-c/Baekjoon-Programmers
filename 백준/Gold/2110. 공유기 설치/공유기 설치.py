import sys
input = sys.stdin.readline

n, c = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
start, end = 1, arr[-1] - arr[0]
res = 0

if c == 2:
  print(end)
else:
  while(start < end):
    mid = (start + end)//2
    count = 1
    current = arr[0]
    
    for i in range(n):
        if arr[i] - current >= mid:
            count+=1
            current = arr[i]
            
    if count >= c:
        start = mid + 1
        res = mid
    elif count < c:
        end = mid
        
  print(res)