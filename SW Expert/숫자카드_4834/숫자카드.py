T = int(input())

for i in range(1, T+1):
    N = int(input())
    a = input()

    A = {}
    for num in a:
        num = int(num)
        if num not in A:
            A[num] = 0
        A[num] += 1
    
    # value 기준으로 내림차순 정렬 후 key 기준으로 내림차순 정렬해주기
    A = sorted(A.items(), key = lambda x : (x[1], x[0]), reverse=True)
    # print(A)
    print('#{} {} {}'.format(i, A[0][0], A[0][1]))