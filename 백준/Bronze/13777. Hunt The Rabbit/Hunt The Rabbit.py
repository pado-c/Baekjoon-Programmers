def binary(start, end, target, arr):
  res = []
  
  while start <= end:
    mid = (start + end) //2
    res.append(arr[mid])
    
    if target == arr[mid]:
      return res
    elif target >= arr[mid]:
      start = mid + 1
    else:
      end = mid - 1
      

arr = [i for i in range(1,51)]
while True:
  target = int(input())
  if target == 0: break
  print(*binary(0,len(arr)-1, target, arr))