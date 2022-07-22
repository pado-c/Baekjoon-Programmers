import sys
n = int(sys.stdin.readline()) #가진 카드 수
n_card = list(map(int,sys.stdin.readline().split())) #가진 card number
nums = {}

for i in n_card:
    if i not in nums: #nums에 없다면 {i : 1}로 추가됨
        nums[i] = 1
    else:   
        nums[i] += 1
    
m = int(sys.stdin.readline()) #비교할 카드 수
m_card = list(map(int,sys.stdin.readline().split())) #비교할 card number

for i in m_card:
    if i not in nums:
        print(0, end=' ')
    else:
        print(nums[i], end=' ')