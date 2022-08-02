import sys
from tabnanny import check
input = sys.stdin.readline
N = int(input())
cmd = [input() for _ in range(N)]

checker = list(cmd[0])

for i in range(N):
    for j in range(len(checker)):
        if cmd[i][j] != checker[j]:
            checker[j] = "?"

print(''.join(checker))