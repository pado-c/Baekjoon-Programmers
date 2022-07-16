A,B = input().split()

reversed_A = ''.join(reversed(A))
reversed_B = ''.join(reversed(B))

if int(reversed_A) > int(reversed_B):
    print(reversed_A)
else:
    print(reversed_B)