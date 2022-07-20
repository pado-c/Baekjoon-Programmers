import sys
n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y = input().split()
    points += [[int(x), int(y)]]

points.sort()

for x, y in points:
    print(x, y)