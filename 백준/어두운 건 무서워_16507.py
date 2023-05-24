def solution():
    R, C, Q = map(int, input().split())
    board = [[0] * (C + 1)]
    for _ in range(R):
        board.append([0] + list(map(int, input().split())))
    for i in range(R + 1):
        for j in range(1, C + 1):
            board[i][j] += board[i][j - 1]

    # for j in range(C):
    #     for i in range(1, R):
    #         board[i][j] += board[i - 1][j]

    # for b in board:
    #     print(b)
    # print()

    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().split())

        scope = (r2 - r1 + 1) * (c2 - c1 + 1)
        total = 0
        for i in range(r1, r2 + 1):
            total += board[i][c2] - board[i][c1 - 1]

        # print(total, scope)
        print(total // scope)


if __name__ == "__main__":
    solution()
