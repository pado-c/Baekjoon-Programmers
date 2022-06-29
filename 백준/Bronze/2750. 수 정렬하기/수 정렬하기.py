N = int(input()) #수의 개수 입력
i = 1
nums= []

while i <= N:
  num = int(input())
  nums += [num]    #입력받은 수 리스트로 모으기
  i+=1
  
nums.sort()   #입력받은 수 정렬
for j in nums:   #하나씩 출력
  print(j)