# A(start)번째 숫자부터 B(end)번째 숫자까지 합
start, end = map(int,input().split()) 
nums = []
num = 1

while True:
  if len(nums) < end: # B번째 자리가 아직 존재하지 않음
    li = [num] * num
    nums.extend(li)
    num += 1
    
  else: # B번째 자리까지 존재함
    nums = nums[start - 1: end]
    print(sum(nums))
    break