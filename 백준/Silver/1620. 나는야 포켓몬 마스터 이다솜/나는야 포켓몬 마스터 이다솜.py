import sys
N,M = sys.stdin.readline().split()  #포켓몬의 개수 N, 문제의 개수 M
pkmDict_int = {}  #입력되는 포켓몬들을 숫자와 연결해 딕셔너리로 변형(0:'Bulbasaur')
pkmDict_str = {}

for i in range (1,int(N)+1):   
    name = sys.stdin.readline().strip()
    pkmDict_int[i] = name
    pkmDict_str[name] = i

for _ in range (int(M)):
    problem = sys.stdin.readline().strip()   #문제 입력
    if problem.isdigit() :  #문제가 숫자열이라면   
        print(pkmDict_int[int(problem)])

    else:  #문제가 문자열이라면
        print(pkmDict_str[problem])  