import sys
input = sys.stdin.readline
A, B =  map(list,input().split())
A = list(map(int,A))
B = list(map(int,B))
print(sum(A) * sum(B))