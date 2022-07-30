import math

#높이 V인 나무 막대 / 낮에는 A만큼 오르고 밤에 B만큼 미끄러짐
A, B, V = map(int,input().split())
# (A-B)*day + A >= V
# day >= (V-A)/(A-B)
day = math.ceil((V-A)/(A-B) + 1)
print(day)