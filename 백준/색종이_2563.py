def solution():
    answer = 0
    N = int(input())

    board = [[0] * 100 for _ in range(100)]
    for _ in range(N):
        x, y = map(int, input().split())
        for i in range(y, y + 10):
            for j in range(x, x + 10):
                if board[i][j] == 0:
                    board[i][j] = 1
                    answer += 1

    # for b in board:
    #     print(b)

    print(answer)


if __name__ == "__main__":
    solution()
