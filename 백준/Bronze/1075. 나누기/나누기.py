n = input()
f = int(input())
num = int(n[:-2] + '00')

while True:
    if num % f == 0:
        print(str(num)[-2:])
        break
    num += 1