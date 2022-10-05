import sys
input = sys.stdin.readline

n = int(input())
array = sorted(list(map(int,input().strip().split())))
print(*array)