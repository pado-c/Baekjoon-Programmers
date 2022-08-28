import sys
input = sys.stdin.readline

N = int(input()) #학생 수
students = []
for _ in range(N):
    n, k, e, m = list(map(str,input().split())) #이름, 국어, 영어, 수학
    students.append([n, int(k), int(e), int(m)])

students.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
# 국어 점수(x[1])이 감소하는 순서
# 국어 점수가 같으면 영어 점수(x[2])가 증가하는 순서
# 국어 점수, 영어 점수가 같으면 수학 점수(x[3])가 감소하는 순서
# 모든 점수가 같으면 이름(x[0])을 사전 순

for student in students:
    print(student[0])