S = int(input())
i = 1
cnt = 0

while S >= i:
    S -= i
    i += 1
    cnt += 1
print(cnt)