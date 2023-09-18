from collections import deque


def solve():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    # for b in board:
    #     print(b)

    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                red = (i, j)
            if board[i][j] == "B":
                blue = (i, j)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]  # visited[red_y][red_x][blue_y][blue_x]

    def bfs():
        q = deque()
        q.append((red, blue, 1))

        while q:
            (ry, rx), (by, bx), count = q.popleft()
            if count > 10:
                return -1

            for d in range(4):
                nry, nrx, rd = move(ry, rx, d)
                nby, nbx, bd = move(by, bx, d)
                # print(nry, nrx, "/", nby, nbx)

                if board[nby][nbx] == "O":
                    continue

                if board[nry][nrx] == "O":
                    return count

                if nry == nby and nrx == nbx:
                    if rd > bd:
                        nry = nry - dy[d]
                        nrx = nrx - dx[d]
                    else:
                        nby = nby - dy[d]
                        nbx = nbx - dx[d]

                if visited[nry][nrx][nby][nbx] == 1:
                    continue

                visited[ry][rx][by][bx] = 1
                q.append(((nry, nrx), (nby, nbx), count + 1))

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

    answer = bfs()
    if not answer:
        return -1
    return answer


if __name__ == "__main__":
    print(solve())
