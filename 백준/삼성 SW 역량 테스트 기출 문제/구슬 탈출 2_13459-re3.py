from collections import deque


def solution():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(N):
        for x in range(M):
            if board[y][x] == "R":
                red = (y, x)
            if board[y][x] == "B":
                blue = (y, x)

    q = deque()
    q.append((red, blue, 1))
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]  # visited[ry][rx][by][bx]

    def move(y, x, d):
        dis = 0

        while True:
            ny = y + dy[d]
            nx = x + dx[d]
            dis += 1
            if board[ny][nx] == "#":
                return (y, x, dis)
            elif board[ny][nx] == "O":
                return (ny, nx, dis)
            else:
                y = ny
                x = nx

    while q:
        (ry, rx), (by, bx), count = q.popleft()
        if count > 10:
            return -1

        for d in range(4):
            nry, nrx, rd = move(ry, rx, d)
            nby, nbx, bd = move(by, bx, d)
            # print(f"{nry} {nrx} / {nby} {nbx} / {d}")

            if board[nby][nbx] == "O":
                continue

            if board[nry][nrx] == "O":
                return count

            if nry == nby and nrx == nbx:
                if rd > bd:
                    nry -= dy[d]
                    nrx -= dx[d]
                else:
                    nby -= dy[d]
                    nbx -= dx[d]

            if visited[nry][nrx][nby][nbx]:
                continue

            visited[ry][rx][by][bx] = 1
            q.append(((nry, nrx), (nby, nbx), count + 1))

    return -1


if __name__ == "__main__":
    print(solution())
