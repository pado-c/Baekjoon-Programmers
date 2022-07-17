import sys

N = int(sys.stdin.readline()) #단어의 개수
wordList = []
for _ in range(N):
    wordList += [sys.stdin.readline()]

set_wordList = list(set(wordList)) #중복된 단어는 제외
set_wordList.sort()  #사전순 정렬
set_wordList.sort(key=len)   #length에 따라 정렬

print(''.join(set_wordList)) 