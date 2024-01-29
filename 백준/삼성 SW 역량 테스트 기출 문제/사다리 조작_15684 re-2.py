"""
15684. 사다리 조작
"""


def solution():
    N, M, H = map(int, input().split())
    if M == 0:
        return 0

    board = [[0] * N for _ in range(H)]

    for _ in range(M):
        a, b = map(int, input().split())
        board[a - 1][b - 1] = 1

    # for b in board:
    #     print(b)
    # print()

    global answer
    answer = 4

    def check():
        for col in range(N):
            c = col
            for row in range(H):
                if c < N and board[row][c]:
                    c += 1
                elif c > 0 and board[row][c - 1]:
                    c -= 1
            if c != col:
                return False
        return True

    def solve(row, col, cnt):
        global answer
        if check():
            answer = min(answer, cnt)
            return

        if cnt >= 3:
            return

        for y in range(row, H):
            if y == row:
                z = col
            else:
                z = 0
            for x in range(z, N - 1):
                # print("#", y, x)
                # for b in board:
                #     print(b)
                # print()
                if board[y][x] == 0 and board[y][x + 1] == 0:
                    board[y][x] = 1
                    solve(y, x + 2, cnt + 1)
                    board[y][x] = 0

    solve(0, 0, 0)

    if answer > 3:
        return -1

    return answer


if __name__ == "__main__":
    print(solution())
