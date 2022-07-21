import sys
import itertools
n, m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split())) #카드 숫자

card_combi = list(itertools.combinations(card, 3)) #카드 3장을 뽑아 만들 수 있는 조합...
max_combiNum = 0 #만들 수 있는 최댓값

for i in card_combi:
    card_sum = sum(i)
    if card_sum <= m:  #m보다 작거나 같아야 함
        if card_sum > max_combiNum:
            max_combiNum = card_sum

print(max_combiNum)