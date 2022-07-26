nums = set(range(1,10001)) #차집합을 위한 set
notInRes = set()   #차집합을 위한 set

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    notInRes.add(i)  #생성자가 존재하는 숫자

res = sorted(nums.difference(notInRes)) # difference - 차집합
for i in res:
    print(i)