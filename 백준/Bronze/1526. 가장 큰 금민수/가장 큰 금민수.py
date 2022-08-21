N = int(input())
num = 0

for n in range(4, N+1):
  n_str = str(n)
  find_four = n_str.count("4")
  find_seven = n_str.count("7")
  
  if len(n_str) == find_four + find_seven:
    num = n
    
print(num)