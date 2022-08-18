n = int(input())

if n == 1:
    print("*")
elif n % 2 == 0:
    for _ in range(n):
        print("* " * (n//2))
        print(" *" * (n//2))
else:
    for _ in range(n):
        print("* " * (n//2 + 1))
        print(" *" * (n//2))