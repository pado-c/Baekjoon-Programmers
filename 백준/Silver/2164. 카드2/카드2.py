import collections
n = int(input())
card = collections.deque([i for i in range(1, n+1)])

while len(card) > 1:
    card.popleft()  # 왼쪽 요소를 제거
    card.rotate(-1) # 왼쪽으로 한칸씩 이동

print(*card)