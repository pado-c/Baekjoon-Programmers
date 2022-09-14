import sys
input= sys.stdin.readline

nA, nB = map(int,input().split())
arrA = set(list(map(int,input().split())))
arrB = set(list(map(int,input().split())))
difference = arrA.difference(arrB)  #set을 이용한 차집합

if len(difference) == 0:
  print(0)
else:
  print(len(difference))
  print(*sorted(difference))