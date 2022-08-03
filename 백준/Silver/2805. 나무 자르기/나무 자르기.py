import sys
input = sys.stdin.readline

N, M = map(int,input().split())  #나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M
trees = list(map(int,input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    tree_length = 0
    
    for i in trees:
        if mid <= i:
            tree_length += i - mid
    
    if tree_length >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)