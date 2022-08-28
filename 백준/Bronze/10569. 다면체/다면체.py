t = int(input())
for _ in range(t):
    V, E = list(map(int,input().split())) #꼭짓점의 개수, 모서리의 개수
    print(2 - V + E) #면의 수