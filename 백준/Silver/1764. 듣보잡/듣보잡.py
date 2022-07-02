N,M = map(int,input().split())
neverHeard = set()
neverSeen = set()

for _ in range (N):
    neverHeard.add(input())

for _ in range (M):
    neverSeen.add(input())

neverHeardSeen = sorted(neverHeard & neverSeen)
#교집합 set1&set2 / sorted로 사전순 정렬

print(len(neverHeardSeen))
for i in neverHeardSeen:
    print(i)