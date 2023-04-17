def solution():
    N, M, K = map(int, input().split())
    board = [[0] * (M + 1) for _ in range(N + 1)]
    # for b in board:
    #     print(b)
    # print()

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if i == 1 and j == 1:
                board[i][j] = 1
                continue
            board[i][j] = board[i - 1][j] + board[i][j - 1]

    # for b in board:
    #     print(b)
    # print()

    if K == 0:
        result = board[-1][-1]
    else:
        row1 = (K - 1) // M + 1
        col1 = K - (row1 - 1) * M
        row2, col2 = N - row1 + 1, M - col1 + 1
        # print(row1, col1)
        # print(row2, col2)
        result = board[row1][col1] * board[row2][col2]

    # print(board[row1][col1])
    print(result)


if __name__ == "__main__":
    solution()
