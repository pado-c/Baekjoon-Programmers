n = int(input())
call = list(map(int,input().split()))

youngmin = list(map(lambda x: (x//30 + 1) * 10, call))
minsik = list(map(lambda x: (x//60 + 1) * 15,call))

youngmin_total = sum(youngmin)
minsik_total = sum(minsik)

if youngmin_total < minsik_total:
  print('Y',youngmin_total)
elif youngmin_total > minsik_total:
  print('M', minsik_total)
else:
  print('Y M', youngmin_total)