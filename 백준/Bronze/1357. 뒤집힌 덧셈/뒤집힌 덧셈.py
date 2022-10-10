x, y = input().split()
reversed_x = int(x[::-1])
reversed_y = int(y[::-1])
print(int(str(reversed_x + reversed_y)[::-1]))