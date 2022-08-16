import sys
input = sys.stdin.readline

def calc_1(): #상하 반전
  temp= []
  for i in range(n-1, -1, -1):
    temp.append(arr[i])
  return temp

def calc_2(): #좌우 반전
  temp = [[0] * m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      temp[i][j] = arr[i][m-1-j]
  return temp

def calc_3(): #오른쪽으로 90도 회전
  temp = [[0] * n for _ in range(m)]
  for i in range(m):
    for j in range(n):
      temp[i][j] = arr[n-1-j][i]
  return temp

def calc_4(): #왼쪽으로 90도 회전
  temp = [[0] * n for _ in range(m)]
  for i in range(m):
    for j in range(n):
      temp[i][j] = arr[j][m - 1 - i]
  return temp

def calc_5():
  temp = [[0] * m for _ in range(n)]
  for i in range(n // 2): # 1 -> 2
    for j in range(m // 2):
      temp[i][j + m//2] = arr[i][j]
  
  for i in range(n // 2): # 2 -> 3
    for j in range(m // 2, m):
      temp[i + n//2][j] = arr[i][j]
  
  for i in range(n // 2, n): # 3 -> 4
    for j in range(m // 2, m):
      temp[i][j - m//2] = arr[i][j]
  
  for i in range(n // 2, n): # 4 -> 1
    for j in range(m // 2):
      temp[i - n//2][j] = arr[i][j]
  
  return temp

def calc_6():
  temp = [[0] * m for _ in range(n)]
  for i in range(n // 2): # 1 -> 4
    for j in range(m // 2):
      temp[i + n//2][j] = arr[i][j]
      
  for i in range(n // 2, n): # 4 -> 3
    for j in range(m // 2):
      temp[i][j + m//2] = arr[i][j]
      
  for i in range(n // 2, n): # 3 -> 2
    for j in range(m // 2, m):
      temp[i - n//2][j] = arr[i][j]
      
  for i in range(n // 2): # 2 -> 1
    for j in range(m // 2, m):
      temp[i][j - m//2] = arr[i][j]
  
  return temp

n, m, r = map(int,input().split()) #배열의 크기가 N × M / 수행해야 하는 연산의 수 R
arr = [list(map(int,input().split())) for _ in range(n)]
oper = list(map(int, input().split())) #수행해야 하는 연산

for o in oper:
  if o == 1:
      arr = calc_1()
  elif o == 2:
      arr = calc_2()
  elif o == 3:
      arr = calc_3()
      n, m = m, n
  elif o == 4:
      arr = calc_4()
      n, m = m, n
  elif o == 5:
      arr = calc_5()
  else:
      arr = calc_6()

for a in arr:
  print(*a)