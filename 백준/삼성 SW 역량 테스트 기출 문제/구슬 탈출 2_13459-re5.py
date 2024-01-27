from collections import deque


def solution():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                red = [i, j]
            elif board[i][j] == "B":
                blue = [i, j]
            elif board[i][j] == "O":
                out = [i, j]

    # 상좌하우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

    def move(y, x, d):
        for i in range(10):  # 보드 최대 크기
            ny = y + dy[d]
            nx = x + dx[d]

            if board[ny][nx] == "#":
                return [y, x, i]
            if board[ny][nx] == "O":
                return [ny, nx, i]

            y = ny
            x = nx

    def bfs(red, blue, visited):
        ry, rx = red
        by, bx = blue
        q = deque()
        q.append([ry, rx, by, bx, 1])

        while q:
            ry, rx, by, bx, cnt = q.popleft()
            # print("@", ry, rx, by, bx, cnt)
            if cnt > 10:
                return -1

            for d in range(4):
                nry, nrx, r_cnt = move(ry, rx, d)
                nby, nbx, b_cnt = move(by, bx, d)
                # print("@@r", nry, nrx, r_cnt, d)
                # print("@@b", nby, nbx, b_cnt, d)

                if nby == out[0] and nbx == out[1]:  # 파란 구슬이 구멍에 빠지면 continue
                    continue

                if nry == out[0] and nrx == out[1]:  # 빨간 구슬이 구멍에 빠지면 이동 횟수 반환
                    return cnt

                if nry == nby and nrx == nbx:  # 빨간 구슬, 파란 구슬이 동일한 위치가 되면 많이 움직인 구슬을 한 칸 반대로 이동
                    if r_cnt > b_cnt:
                        nry -= dy[d]
                        nrx -= dx[d]
                    else:
                        nby -= dy[d]
                        nbx -= dx[d]

                if visited[nry][nrx][nby][nbx] == 0:
                    q.append([nry, nrx, nby, nbx, cnt + 1])
                    visited[nry][nrx][nby][nbx] = 1

    answer = bfs(red, blue, visited)

    if answer:
        return answer
    return -1


if __name__ == "__main__":
    print(solution())
