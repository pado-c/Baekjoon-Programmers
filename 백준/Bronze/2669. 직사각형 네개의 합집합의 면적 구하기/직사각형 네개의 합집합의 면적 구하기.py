graph = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

res = sum(graph,[]) # [[0, 0], [0, 0]] => [0, 0, 0, 0]
print(res.count(1)) # res list에 1이 몇 개 존재하는 지