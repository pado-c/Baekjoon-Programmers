score = 0

for _ in range(5):
    s = int(input())
    if s >= 40: score += s
    else: score += 40

print(score//5)