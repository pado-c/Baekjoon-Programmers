string = input()
dict = {
    "ABC" : 2,
    "DEF" : 3,
    "GHI" : 4,
    "JKL" : 5,
    "MNO" : 6,
    "PQRS" : 7,
    "TUV" : 8,
    "WXYZ" : 9,
}

res = len(string)
for i in string:
    for j in dict:
        if i in j:
            res += dict[j]
            
print(res)