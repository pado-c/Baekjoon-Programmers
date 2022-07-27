croatia_alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
string = input()

for i in croatia_alpha:
    if i in string:
        string = string.replace(i,'0')
        
print(len(string))