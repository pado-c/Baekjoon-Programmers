n = int(input()) #num of members
member = []
for _ in range(n):
    age, name = map(str,input().split())
    age = int(age)
    member.append([age, name])

member.sort(key = lambda x: x[0]) #나이 오름차순으로 정렬

for i in member:
    print(*i)