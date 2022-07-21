while True:
    triangle = list(map(int,input().split()))
    if triangle == [0, 0, 0]: #0 0 0 입력 시 종료
        break

    triangle.sort(reverse = True) #내림차순 정렬
    x,y,z = triangle #x가 가장 큰 수, z가 가장 작은 수

    if x**2 == y**2 + z**2: #피타고라스
        print('right')
    else:
        print('wrong')