arr = [int(input()) for _ in range(9)]
sum = sum(arr)
out1, out2 = 0, 0

for i in range(8):
    for j in range(i+1, 9):
        if sum - (arr[i] + arr[j]) == 100:
            out1 = arr[i]
            out2 = arr[j]
            
arr.remove(out1)
arr.remove(out2)

arr.sort()
for i in arr:
    print(i)