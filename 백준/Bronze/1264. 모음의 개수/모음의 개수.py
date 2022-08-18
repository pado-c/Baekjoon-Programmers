while True:
    str = input()
    if str == "#":
        break
    else:
        lower_str = str.lower() #소문자로 통일
        cnt = 0
        for s in lower_str:
            if s in "aeiou":
                cnt += 1
                
        print(cnt)