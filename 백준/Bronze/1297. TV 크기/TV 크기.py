#TV의 대각선 길이 D, TV의 높이 비율 H, TV의 너비 비율 W
D, H, W = list(map(int,input().split()))

X = D / ((H ** 2 + W ** 2) ** 0.5)

h = int(H * X)
w = int(W * X)
print(h, w)