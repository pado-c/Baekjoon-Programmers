import sys
input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

#끝나는 시간 - 시작 시간 순으로 정렬
meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 0
endTime = 0

for s, e in meeting:
  if s >= endTime: # 그 전 회의가 끝나고 난 후에 시작 가능...
    cnt += 1
    endTime = e
    
print(cnt)