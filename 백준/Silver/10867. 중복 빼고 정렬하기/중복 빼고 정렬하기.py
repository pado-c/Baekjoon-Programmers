n = int(input())
nums = list(map(int,input().split()))
nums = list(set(nums)) #중복 제거
nums.sort() #오름차순 정렬
print(*nums)