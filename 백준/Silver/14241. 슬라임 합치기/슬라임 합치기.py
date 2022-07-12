N = int(input())
size = list(map(int,input().split()))
sum_size = 0
score = 0

size.sort(reverse=True)
for i in range(0,N-1):
    if i == 0:
        score += size[i] * size[i+1]
        sum_size = size[i] + size[i+1]
    else:
        score += sum_size * size[i+1]
        sum_size += size[i+1]
        
print(score)