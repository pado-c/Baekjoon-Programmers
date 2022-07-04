S = input()
res = []
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for a in alpha:
    if a in S:
        res.append(S.index(a))
    elif a not in S:
        res.append(-1)

print(*res)