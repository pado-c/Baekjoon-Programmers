import string
import sys

word = sys.stdin.readline().upper()   #입력된 문자열 대문자로
alphabet = list(string.ascii_uppercase) #알바벳 대문자 리스트
cnt = 0  #가장 많이 사용된 수
idx = 'idx'   #cnt의 index
sub_idx = 'No'   #cnt만큼 사용된 알파벳이 또 있는지

for i in range(len(alphabet)):
    if word.count(alphabet[i]) > cnt:  #가장 많이 사용된 알파벳일 경우
        cnt = word.count(alphabet[i])
        idx = i
        sub_idx = 'No'
    elif word.count(alphabet[i]) == cnt and cnt > 0: #동일하게 사용된 알파벳일 경우
        sub_idx = 'Yes'
    else:
        continue

if sub_idx != 'No' :
    print('?')
else:
    print(alphabet[idx])