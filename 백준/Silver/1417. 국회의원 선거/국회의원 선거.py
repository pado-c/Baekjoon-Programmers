n = int(input()) #후보자 수
num1_vote = int(input())  #기호1번
vote = [int(input().strip()) for _ in range(n-1)]  #나머지 번호
cnt = 0

vote.sort(reverse=True) #내림차순 정렬(10,9...)
if n == 1: #후보가 1번뿐인 경우
    print(0)
else:
    while num1_vote <= vote[0]:  #가장 표 수가 많은 후보와 기호1번의 표 수 비교
        vote[0] -= 1  #가장 표가 많은 후보 것 1장 빼돌림
        num1_vote += 1
        cnt += 1
        vote.sort(reverse=True)  #다시 내림차순 정렬(10,9...)
    print(cnt)