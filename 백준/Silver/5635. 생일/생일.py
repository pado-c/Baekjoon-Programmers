import sys
input = sys.stdin.readline

n = int(input())
birthday = []
for _ in range(n):
  birthday.append(input().split())  # [name. day, month, year]

birthday.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1]))) # x[3] = year, x[2] = month, x[1] = day

print(birthday[n-1][0]) #가장 나이가 적은 사람
print(birthday[0][0]) # 가장 나이가 많은 사람 