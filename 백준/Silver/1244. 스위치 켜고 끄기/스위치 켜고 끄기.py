switch_cnt = int(input())  #스위치 개수
switch_state = [0] + list(map(int,input().split()))  #스위치 상태
student_cnt = int(input())  #학생 수
student = []  
for _ in range(student_cnt):
    student += [list(map(int,input().split()))] # [학생 성별, 학생이 받은 수]

for i in student:
    if i[0] == 1:  #남학생
        for j in range(1,switch_cnt+1):
            if j % i[1] == 0:  #j가 남학생이 받은 수의 배수일 때
                if switch_state[j] == 0: #j번째 스위치가 꺼져있다면
                    switch_state[j] = 1
                else:                    #j번째 스위치가 켜져있다면
                    switch_state[j] = 0

    elif i[0] == 2: #여학생
        for j in range(i[1]):
            if i[1] + j > switch_cnt or i[1] - j < 1:
                break

            if switch_state[i[1] - j] == switch_state[i[1] + j]: 
            #받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭
                if switch_state[i[1] - j] == 0: #스위치가 꺼져있다면
                    switch_state[i[1] - j] = 1
                    switch_state[i[1] + j] = 1
                else:                    #스위치가 켜져있다면
                    switch_state[i[1] - j] = 0
                    switch_state[i[1] + j] = 0
                    
            else:   #대칭이 아니면
                break
            
for i in range(1,switch_cnt+1):
    print(switch_state[i], end = " ")
    if i % 20 == 0:  # 20개 이상이면 줄바꿈
        print()