#2진수를 다시 숫자로 변환
n = int('0b' + input(), 2)
#format() 내장 함수를 이용해 숫자를 다른 진수의 문자열로 바꿀 때 접두어를 제외
res = format(n, 'o')
print(res)