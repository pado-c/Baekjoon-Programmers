k = int(input())

num = [0] * (k+1)
num[1] = 1

for i in range(2, k+1):
  num[i] = num[i-1] + num[i-2]
  
print(num[k-1], num[k])