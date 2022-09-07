from fractions import Fraction #분수 계산 모듈

n = int(input())
ring = list(map(int,input().split()))
standard = Fraction(ring[0],1)

for r in ring[1:]:
  f= standard / Fraction(r,1)
  a = f.numerator #분자
  b = f.denominator #분모
  
  print(f'{a}/{b}')