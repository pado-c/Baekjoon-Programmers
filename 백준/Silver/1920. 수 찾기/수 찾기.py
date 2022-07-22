import sys
n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
counter = {}

for i in n_list:
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] += 1

m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

for i in m_list:
    if i in counter:
        print(1)
    else:
        print(0)