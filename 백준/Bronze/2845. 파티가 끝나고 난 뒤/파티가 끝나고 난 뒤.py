import sys
input = sys.stdin.readline
L, P = map(int,input().split())
inPosts = list(map(int,input().split()))
Sangguen = L * P

for i in inPosts:
    print(i - Sangguen)