"""
재귀 너무 어렵다...

가장 큰 원반을 제외한 나머지 모든 원반을 보조 기둥으로 옮기기
"""

N = int(input())

move = []

# 1번 원판에서 3번 원판으로 옮겨야 함
# 1, 2, 3 차례대로 a, b, c
def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])     # n이 짝수이면 a, c가 각각 1, 2이 되고 홀수이면 a, c가 각각 1, 3이 됨
                                # 즉, n이 짝수이면 원판을 처음으로 옮길 때 1번 기둥에서 2번 기둥으로 옮겨지고 홀수이면 1번 기둥에서 3번 기둥으로 옮겨짐
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)

hanoi(N, 1, 2, 3)
print(len(move))
print('\n'.join(f"{a} {b}" for a, b in move))