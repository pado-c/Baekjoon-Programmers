eat = 0  #먹은 버섯 점수
mushroom = [int(input()) for _ in range(10)]

for i in mushroom:
    eat += i
    if eat >= 100:
        if eat - 100 > 100 - (eat - i): # 100에 더 가까운 숫자 찾기
            eat -= i
        break

print(eat)