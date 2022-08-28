import sys
input = sys.stdin.readline

sg = int(input()) #상근이 가진 카드 개수
sg_card = list(map(int,input().split()))
diff = int(input()) #구분해야 할 카드 개수
diff_card = list(map(int,input().split()))

dict = {diff_card[i] : 0 for i in range(diff)}

for i in range(sg):
    if sg_card[i] in dict.keys():
        dict[sg_card[i]] += 1

res = list(dict.values())
print(*res)