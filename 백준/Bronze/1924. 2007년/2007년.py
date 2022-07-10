x,y = map(int,input().split())
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
month = [31,28,31,30,31,30,31,31,30,31,30,31]
today = 0

for i in range (0,x-1):  #1월~ x-1월 까지의 날짜 합(x가 1월이면 합X)
    today += month[i]

today = (today + y) % 7  #날짜 합 + y일 을 7로 나눈 나머지가 요일
print(day[today])