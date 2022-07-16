T = int(input()) #테스트 케이스 개수
RS = []  #[반복횟수 ,반복할 문자열]

for _ in range (T):  # T번 입력받기
    RS += [input().split()]

for i in range(T):
    result = ''
    repeat = int(RS[i][0]) #반복횟수
    for string in list(RS[i][1]):  #반복할 문자열 한글자씩 string에 대입
        result += repeat * string
    
    print(result)