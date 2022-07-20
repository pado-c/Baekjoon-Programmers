n = int(input())
points = []
for _ in range(n):
    x, y = input().split()
    points += [[int(y), int(x)]] #y값으로 정렬해야하므로 y부터

points.sort()

for y, x in points:
    print(x, y)