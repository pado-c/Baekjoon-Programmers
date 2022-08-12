import sys
input = sys.stdin.readline

n = int(input()) #집의 수
house = [list(map(int,input().split())) for _ in range(n)] #집을 칠하는 비용

for i in range(1, n):
  # i번 집의 색은 i-1,i+1번 집의 색과 같지 않아야 함
  # 색이 같지 않은 경우 중 비용이 작은 경우를 더한 상태...
  house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
  house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
  house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]
  
print(min(house[n-1]))