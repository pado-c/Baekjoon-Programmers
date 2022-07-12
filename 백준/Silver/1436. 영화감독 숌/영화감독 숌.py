N = int(input())
basic = 666

while True:
    if '666' in str(basic):
        N -= 1
    if N == 0:
        print(basic)
        break
    basic += 1