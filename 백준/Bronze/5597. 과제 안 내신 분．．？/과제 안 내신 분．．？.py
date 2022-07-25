person = list(map(lambda x: x, range(1,31))) #출석번호는 1번부터 30번

for _ in range(28): #그 중 28명만 제출
    n = int(input())
    person.remove(n)

for i in sorted(person):
    print(i)