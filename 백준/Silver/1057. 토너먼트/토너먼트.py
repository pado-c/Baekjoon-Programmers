N, jm, hs = map(int,input().split()) #참가자 수, 지민의 번호, 한수의 번호
rnd = 0  #라운드번호

while jm != hs:
    jm -= jm//2
    hs -= hs//2
    rnd += 1
    #jm = 8 / hs = 9일 때 토너먼트가 진행되면 번호는...
    #jm은 8 > 4 > 2 > 1 > 1
    #hs는 9 > 5 > 3 > 2 > 1
    #jm과 hs의 번호가 같아지면 만났다는 의미.

print(rnd)