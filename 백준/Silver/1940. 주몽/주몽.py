n = int(input())
m = int(input())
nums = sorted(list(map(int,input().split())))

cnt = 0
start = 0
end = n-1

while start != end:
  sum = nums[start] + nums[end]
  if sum == m:
    cnt += 1
    start += 1
  elif sum > m:
    end -= 1
  else:
    start += 1

print(cnt)