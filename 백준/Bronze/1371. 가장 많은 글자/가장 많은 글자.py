import sys

string = sys.stdin.read()
alphabet = [0 for _ in range(26)]
for i in string:
    if i.islower():
        alphabet[ord(i) - 97] += 1
        # a의 아스키코드는 97

for i in range(26):
    if alphabet[i] == max(alphabet):
        print(chr(i+97),end="")