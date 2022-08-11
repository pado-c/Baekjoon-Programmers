s = input()
cnt = 0
num = 2  #비교를 위한 임의의 값 설정(0, 1 이 아닌 값으로 설정)

for i in s:
  if i != num:
    num = i
    cnt += 1

print(cnt//2)