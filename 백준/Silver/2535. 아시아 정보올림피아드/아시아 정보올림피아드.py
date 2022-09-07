n = int(input())
student = [list(map(int,input().split())) for _ in range(n)]
student.sort(key=lambda x: -x[2]) #성적을 기준으로 내림차순 정렬

dict = {} #메달 개수
cnt = 0 

for st in student:
  if st[0] in dict:
    dict[st[0]] += 1
  else:
    dict[st[0]] = 1
  
  if dict[st[0]] <= 2: #메달 개수가 2개 이하인 경우 출력
    cnt += 1
    print(*st[:2])

  if cnt == 3:
    break