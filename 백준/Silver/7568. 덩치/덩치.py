N = int(input()) #전체 사람 수
xy_list = [] #입력받은 정보
result = [] #등수 저장

for _ in range (N):
    xy_list += [list(map(int,input().split()))]

for i in range(N):
    base = 1  # 1등부터 시작
    for j in range(N):
        if xy_list[i][0] < xy_list[j][0] and xy_list[i][1] < xy_list[j][1]:
            base += 1  #덩치가 작으면 등수 +1
    result.append(str(base)) #join을 위해 str로 변형

print(' '.join(result)) #문자열 사이에 공백을 넣어 출력