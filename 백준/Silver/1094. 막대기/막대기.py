X = int(input())
box = [32,16,8,4,2,1]
cnt = 0

if X == 64:
    print(1)

elif X < 64:
    for i in range(len(box)):
        X -= box[i]
        if X == 0:
            cnt += 1
            print(cnt)
            break

        elif X < 0:
            X += box[i]
            continue
        
        elif X > 0:
            cnt += 1
            continue