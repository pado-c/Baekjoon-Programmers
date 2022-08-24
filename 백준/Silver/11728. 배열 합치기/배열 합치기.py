a_n, b_n = map(int,input().split())

li = []
for _ in range(2):
  num = list(map(int,input().split()))
  li.extend(num)
  
li.sort() #정렬
set(li) #중복제거
print(*li)