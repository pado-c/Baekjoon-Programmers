N = int(input())
res = 0
for i in range(1,N+1):
    nums = list(map(int,str(i)))
    sumNums = i + sum(nums)
    if N == sumNums:
        res = i
        break
print(res)