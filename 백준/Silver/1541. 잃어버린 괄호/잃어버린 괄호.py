str = input().split('-') # - 기준으로 분리
nums = []

for i in str: # 분리된 숫자들끼리 더함
  num = 0
  m = i.split('+')
  for j in m:
    num += int(j)
  nums.append(num)

res = nums[0]  
for i in range(1,len(nums)):  #더해놓은 원소들끼리 빼기
  res -= nums[i]
print(res)