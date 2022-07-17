K = int(input())
K_list = []

for _ in range(K):
    k = int(input())
    if k == 0:
        K_list.pop()
    else:
        K_list += [k]

print(sum(K_list))