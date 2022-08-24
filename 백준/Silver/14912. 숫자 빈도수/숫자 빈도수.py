n, d = map(int,input().split())

num_string = ""

for i in range(1, n+1):
  num_string += str(i)

print(num_string.count(str(d)))