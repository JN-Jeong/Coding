while True:
    n1, n2 = map(int, input().split())

    if n1 == 0 and n2 == 0:
        break

    # 두 수가 같은 경우는 없음
    if n1 > n2:
        if n1 % n2 == 0:
            print('multiple')
        else:
            print('neither')
    else:
        if n2 % n1 == 0:
            print('factor')
        else:
            print('neither')
            