for i in range(1,int(input())+1):
  score = sorted(list(map(int,input().split()))[1:])
  
  gap_list = []
  for j in range(len(score) -1):
    gap = score[j+1] - score[j]
    gap_list.append(gap)
    
  print(f"Class {i}")
  print(f"Max {max(score)}, Min {min(score)}, Largest gap {max(gap_list)}")
