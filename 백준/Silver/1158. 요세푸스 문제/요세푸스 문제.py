N,K = map(int,input().split())
person = list(range(1,N+1))
res = []
index = 0

while len(person):
    index += K-1
    #인덱스의 길이가 사람 수 보다 많으면
    if index >= len(person):
        index = index % len(person)
    #해당 인덱스의 사람을 추출해, res에 추가
    res.append(person.pop(index))

print(f"<{', '.join(map(str,res))}>")