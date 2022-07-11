n, newscore, p =map(int,input().split())  #점수 개수, 새로운 점수, 몇등까지 랭커인지
if n == 0:
    print(1)

else:
    ranking = list(map(int,input().split()))  #현재 랭킹 상황
    ranking.append(newscore)
    ranking.sort(reverse=True)

    res = ranking.index(newscore) +1
    if res > p:
        print(-1)
    else:
        if n == p and newscore == ranking[-1]:
            print(-1)
        else:
            print(res)