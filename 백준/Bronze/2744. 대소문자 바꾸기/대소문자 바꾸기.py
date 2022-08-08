str = list(input())
res = ""
for i in str:
    if i.isupper() == True: # 대문자면
        res += i.lower()
    else: #소문자면
        res += i.upper()
print(res)