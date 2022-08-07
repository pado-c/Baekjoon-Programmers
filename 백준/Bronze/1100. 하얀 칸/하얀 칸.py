import sys

input = sys.stdin.readline
chess = [input().rstrip() for _ in range(8)]
res = 0

for i in range(8):
    c = chess[i]
    if i%2 == 0: #첫 칸이 white
        for j in range(0,8,2):
            if c[j] == "F":
                res += 1         
    else: #첫 칸이 black
        for j in range(1,8,2):
            if c[j] == "F":
                res += 1

print(res)