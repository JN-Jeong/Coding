from collections import deque


def solution():
    N = int(input())
    board = [[0] * N for _ in range(N)]
    board[0][0] = 1
    snake = deque()
    snake.append([0, 0])

    K = int(input())
    for _ in range(K):
        row, col = map(int, input().split())
        board[row - 1][col - 1] = 2

    # 상우하좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    L = int(input())
    directions = {}
    for _ in range(L):
        X, C = input().split()
        X = int(X)
        if C == "L":
            directions[X] = -1
        elif C == "D":
            directions[X] = 1

    d = 1
    y, x = 0, 0
    t = 0
    while True:
        t += 1
        ny = y + dy[d]
        nx = x + dx[d]

        if not (0 <= ny < N and 0 <= nx < N):
            break

        if board[ny][nx] == 0:
            board[ny][nx] = 1
            snake.append([ny, nx])
            row, col = snake.popleft()
            board[row][col] = 0
        elif board[ny][nx] == 1:
            break
        elif board[ny][nx] == 2:
            board[ny][nx] = 1
            snake.append([ny, nx])

        y = ny
        x = nx

        if t in directions:
            d = (d + directions[t]) % 4

    return t


if __name__ == "__main__":
    print(solution())
