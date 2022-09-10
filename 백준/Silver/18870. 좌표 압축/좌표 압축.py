import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
x_set = list(set(arr)) # 중복제거 후, 정렬을 위해 다시 리스트로
x_set.sort() #오름차순 정렬

dict = {}
for i in range(len(x_set)):
  dict[x_set[i]] = i

for i in arr:
  print(dict[i], end=' ')