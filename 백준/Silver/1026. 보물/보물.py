N = int(input())
A = list(map(int,input().split()))   #입력된 문자열을 숫자형 리스트로 변형
B = list(map(int,input().split()))   #입력된 문자열을 숫자형 리스트로 변형
res = 0   #출력을 위한 변수

for i in range (N):
    res += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
    #res = A 리스트에서 가장 작은 수 * B 리스트에서 가장 큰 수
    #list.pop()을 통해 반환된 후 list에서 해당 원소는 삭제됨
print(res)