Acnt,Bcnt = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
#set 메서드와 연산자를 통해 대칭차집합을 구할 수 있다.

print(len(A^B))
# print(len(A.symmetric_difference(B)))
# 위처럼도 가능