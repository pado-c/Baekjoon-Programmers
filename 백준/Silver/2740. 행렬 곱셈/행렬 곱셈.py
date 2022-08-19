#행렬 A의 각 행에 있는 원소를 행렬 B의 각 열에 있는 원소와 곱하여 더한 값
import sys
input = sys.stdin.readline

def calc_list(F_list, S_list):
  res = [[0]*k for _ in range(n)]
  for i in range(n):
    for j in range(k):
      for l in range(m):
        res[i][j] += F_list[i][l] * S_list[l][j]
  return res

if __name__ == "__main__":
  n, m = map(int,input().split())
  F_list = [list(map(int,input().split())) for _ in range(n)]
  
  m, k = map(int,input().split())
  S_list = [list(map(int,input().split())) for _ in range(m)]
  
  res = calc_list(F_list, S_list)
  
  for li in res:
    print(*li)