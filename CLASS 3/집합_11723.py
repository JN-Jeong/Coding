'''
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 

입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.

예제 입력1
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

예제 출력1
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
'''
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