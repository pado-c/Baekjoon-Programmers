import sys
input = sys.stdin.readline

m, n = map(int,input().split())
nums = list(map(int,input().split()))
numSum = [0]
temp = 0
for i in nums:
  temp += i
  numSum.append(temp)
  
for _ in range(n):
  i, j = map(int,input().split())
  print(numSum[j] - numSum[i-1])