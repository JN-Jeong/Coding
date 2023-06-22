from collections import deque


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = N * M

    cctvs = []
    for i in range(N):
        for j in range(M):
            if 1 <= board[i][j] <= 5:
                cctvs.append((i, j))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # q = deque()
    # q.extend(cctvs)
    # print(q)
    # print(q.popleft())

    def watch(row, col, d):
        result = 0
        nrow = row
        ncol = col

        while True:
            nrow += dy[d]
            ncol += dx[d]
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M:
                break

            if board[nrow][ncol] == 6:
                break

            if board[nrow][ncol] == 0:
                result += 1

        return (result, d)

    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:
                result = 0
                for d in range(4):
                    res, direction = watch(r, c, d)
                    print(res, direction)
                    if result < res:
                        result = res
                        now_d = direction

                nr = r
                nc = c
                for i in range(1, result + 1):
                    nr += dy[now_d] * i
                    nc += dx[now_d] * i
                    board[nr][nc] = 7

            elif board[r][c] == 2:
                result = []
                result1 = 0
                for d in [0, 1]:
                    res, direction = watch(r, c, d)
                    result1 += res
                result.append((result1, [0, 1]))

                result2 = 0
                for d in [2, 3]:
                    res, direction = watch(r, c, d)
                    result2 += res
                result.append((result2, [2, 3]))

                result.sort(key=lambda x: -x[0])
                for d in result[0][1]:
                    nr = r
                    nc = c
                    for i in range(1, result + 1):
                        nr += dy[d] * i
                        nc += dx[d] * i
                        board[nr][nc] = 7

            elif board[r][c] == 3:
                result = []
                result1 = 0
                for d in [0, 3]:
                    res, direction = watch(r, c, d)
                    result1 += res
                result.append((result1, [0, 3]))

                result2 = 0
                for d in [1, 3]:
                    res, direction = watch(r, c, d)
                    result2 += res
                result.append((result2, [1, 3]))

                result3 = 0
                for d in [1, 2]:
                    res, direction = watch(r, c, d)
                    result3 += res
                result.append((result3, [1, 2]))

                result4 = 0
                for d in [0, 2]:
                    res, direction = watch(r, c, d)
                    result4 += res
                result.append((result4, [0, 2]))

                result.sort(key=lambda x: -x[0])
                for d in result[0][1]:
                    nr = r
                    nc = c
                    for i in range(1, result + 1):
                        nr += dy[d] * i
                        nc += dx[d] * i
                        board[nr][nc] = 7

            elif board[r][c] == 4:
                result = []
                result1 = 0
                for d in [0, 2, 3]:
                    res, direction = watch(r, c, d)
                    result1 += res
                result.append((result1, [0, 2, 3]))

                result2 = 0
                for d in [0, 1, 3]:
                    res, direction = watch(r, c, d)
                    result2 += res
                result.append((result2, [0, 1, 3]))

                result3 = 0
                for d in [1, 2, 3]:
                    res, direction = watch(r, c, d)
                    result3 += res
                result.append((result3, [1, 2, 3]))

                result4 = 0
                for d in [0, 1, 2]:
                    res, direction = watch(r, c, d)
                    result4 += res
                result.append((result4, [0, 1, 2]))

                result.sort(key=lambda x: -x[0])
                for d in result[0][1]:
                    nr = r
                    nc = c
                    for i in range(1, result + 1):
                        nr += dy[d] * i
                        nc += dx[d] * i
                        board[nr][nc] = 7

            elif board[r][c] == 5:
                for d in range(4):
                    nr = r
                    nc = c
                    for i in range(1, result + 1):
                        nr += dy[d] * i
                        nc += dx[d] * i
                        board[nr][nc] = 7

    for b in board:
        print(b)
    print()


if __name__ == "__main__":
    solution()


"""
상하좌우
03, 13, 12, 02
상우, 우하, 좌하, 좌상

023, 013, 123, 012
상우좌, 상우하, 우하좌, 하좌상
"""
