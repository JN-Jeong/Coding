import sys

M = int(sys.stdin.readline())

S = set()
for i in range(M):
    input_ = sys.stdin.readline().split()

    if len(input_) == 1:
        if input_[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif input_[0] == 'empty':
            S = set()
    else:
        com, num = input_[0], int(input_[1])
        if com == 'add':
            S.add(num)
        elif com == 'remove':
            S.discard(num) # discard 대신 remove 메소드를 쓰면 해당 원소가 존재하지 않을 때 KeyError 발생
        elif com == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif com == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)