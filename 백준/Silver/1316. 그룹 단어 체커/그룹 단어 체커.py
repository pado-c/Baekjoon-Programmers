N = int(input())  #입력할 단어 개수
wordList = list(input().strip() for i in range (N))  #입력한 단어 리스트
check, group = '', []   #확인용  check, 확인 후 그룹단어를 모을 group

for i in wordList:
    for j in range(len(i)):  
        if i[j] not in check:  #check 안에 i[j]가 없을 시
          check += i[j]
        elif i[j] in check and i[j] == check[-1]: #check에 있지만, 바로 전에 추가된 경우일 때(연속)
          check += i[j]
        else:  
          continue
      
    if check == i:  #check가 단어 i와 같다면
        group += [i]   #i는 그룹단어이므로 group에 추가
    check = ''   #check는 초기화(i 다음에 올 단어도 확인해야 함)
    
print(len(group))  #그룹단어의 수