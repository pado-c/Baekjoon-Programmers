board = input()
board = board.replace("XXXX", "AAAA") #XXXX를 AAAA로 치환
board = board.replace("XX", "BB") #XX를 BB로 치환

if board.count('X'): #작업 후에도 X가 남아있다면
  print(-1)

else:
  print(board)
