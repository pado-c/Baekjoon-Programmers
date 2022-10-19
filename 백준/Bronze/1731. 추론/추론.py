import sys
input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))

arithmetical = nums[1] - nums[0] #등차수열
geometric = nums[1]//nums[0] #등비수열

if nums[2] - nums[1] == arithmetical:
  print(nums[-1] + arithmetical)
else:
  print(nums[-1] * geometric)