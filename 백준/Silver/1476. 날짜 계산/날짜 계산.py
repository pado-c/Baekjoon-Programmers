e, s, m = map(int, input().split())
E, S, M = 1, 1, 1
cnt = 1

while True:
    if e == E and s == S and m == M:
        break
    
    E += 1
    S += 1
    M += 1
    
    if E == 16:
        E = 1
    if S == 29:
        S = 1
    if M == 20:
        M = 1
    
    cnt += 1

print(cnt)