from collections import deque


def solution():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                red = [i, j]
            elif board[i][j] == "B":
                blue = [i, j]

    # for b in board:
    #     print(b)

    # 구슬이 이동 할 수 있는지 판단 (이동 할 수 없다면 0, 있다면 1, goal이면 2 반환)
    def is_wall(y, x):
        if board[y][x] == "O":
            return 2
        elif y >= len(board) or x >= len(board[0]) or y < 0 or x < 0 or board[y][x] == "#":
            return 0
        else:
            return 1

    # 구슬 움직이기
    def move(y, x, dir):  # y, x : 위치, dir : 방향, dis : 이동거리
        dis = 0
        while True:
            ny = y + dy[dir]
            nx = x + dx[dir]
            dis += 1

            f = is_wall(ny, nx)
            if f == 0:  # 더 이상 이동할 수 없다면 x, y 반환
                return (y, x, dis)
            elif f == 2:
                return (ny, nx, dis)
            else:  # 이동할 수 있다면 이동
                y = ny
                x = nx

    # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]  # [red_y][red_x][blue_y][blue_x]
    q = deque()
    q.append([*red, *blue, 0])  # 빨간 구슬 좌표(y, x), 파란 구슬 좌표(y, x), 횟수(count), visited
    # print(q)

    while q:
        ry, rx, by, bx, cnt = q.popleft()
        if cnt >= 10:
            return 0

        for i in range(4):
            nry, nrx, rdis = move(ry, rx, i)  # 빨간 구슬
            nby, nbx, bdis = move(by, bx, i)  # 파란 구슬

            if board[nby][nbx] == "O":  # 파란 구슬이 출구에 도착하면 안됨
                continue

            if board[nry][nrx] == "O":  # 빨간 구슬이 출구에 도착하면 return 1
                return 1

            if nry == nby and nrx == nbx:  # 빨간 구슬과 파란 구슬이 같은 칸에 있으면 안됨
                if rdis > bdis:
                    nry = nry - dy[i]
                    nrx = nrx - dx[i]
                else:
                    nby = nby - dy[i]
                    nbx = nbx - dx[i]

            if visited[nry][nrx][nby][nbx] == 1:
                continue

            visited[ry][rx][by][bx] = 1
            q.append([nry, nrx, nby, nbx, cnt + 1])
            # print(y1, x1, y2, x2, cnt)
            # for b in temp_visited:
            #     print(b)
            # print()

    return 0


if __name__ == "__main__":
    print(solution())
