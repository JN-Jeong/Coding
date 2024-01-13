"""
1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다
"""


def solution():
    N, M, K = map(int, input().split())
    fireballs = [list(map(int, input().split())) for _ in range(M)]

    board = [[[] for _ in range(N)] for _ in range(N)]

    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for fireball in fireballs:
        r, c, m, s, d = fireball
        board[r - 1][c - 1].append([m, s, d])

    # for b in board:
    #     print(b)
    # print()

    for _ in range(K):
        # 1. 파이어볼 이동
        temp_board = [[[] for _ in range(N)] for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if board[y][x]:
                    for z in range(len(board[y][x])):
                        m, s, d = board[y][x][z]
                        ny = (y + dy[d] * s) % N
                        nx = (x + dx[d] * s) % N
                        temp_board[ny][nx].append([m, s, d])

        board = [t[:] for t in temp_board]

        # 2. 2개 이상의 파이어볼
        for y in range(N):
            for x in range(N):
                if len(board[y][x]) >= 2:
                    temp_m = 0
                    temp_s = 0
                    odd = 0
                    even = 0
                    num_fireball = len(board[y][x])
                    for _ in range(num_fireball):
                        m, s, d = board[y][x].pop()
                        temp_m += m
                        temp_s += s
                        if d % 2 == 0:
                            even += 1
                        else:
                            odd += 1

                    temp_m //= 5
                    if temp_m > 0:
                        temp_s //= num_fireball

                        if odd == num_fireball or even == num_fireball:  # 방향이 모두 홀수거나 짝수
                            for d in range(0, 8, 2):
                                board[y][x].append([temp_m, temp_s, d])
                        else:
                            for d in range(1, 8, 2):
                                board[y][x].append([temp_m, temp_s, d])

        # for b in board:
        #     print(b)
        # print()

    answer = 0
    for y in range(N):
        for x in range(N):
            for b in board[y][x]:
                answer += b[0]

    return answer


if __name__ == "__main__":
    print(solution())
