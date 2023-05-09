def solution():
    R, C, M = map(int, input().split())
    board = [[[] for _ in range(C)] for _ in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r - 1][c - 1] = [s, d - 1, z]  # 속력, 방향, 크기

    # for b in board:
    #     print(b)
    # print()

    # 상 하 우 좌
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    answer = 0

    for x in range(C):
        # 낚시왕 이동 및 상어 잡기
        for y in range(R):
            if board[y][x]:
                answer += board[y][x][-1]
                board[y][x] = []
                break

        # 상어 이동
        temp = [[[] for _ in range(C)] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                row, col = r, c
                if board[row][col]:
                    s, d, z = board[row][col]

                    for _ in range(s):
                        nrow = row + dy[d]
                        ncol = col + dx[d]

                        if not (0 <= nrow < R and 0 <= ncol < C):
                            if d == 0:
                                d = 1
                            elif d == 1:
                                d = 0
                            elif d == 2:
                                d = 3
                            elif d == 3:
                                d = 2
                            nrow = row + dy[d]
                            ncol = col + dx[d]

                        row = nrow
                        col = ncol

                    if s > 0:
                        if temp[nrow][ncol]:
                            temp_s, temp_d, temp_z = temp[nrow][ncol]
                            if temp_z < z:
                                temp[nrow][ncol] = [s, d, z]
                        else:
                            temp[nrow][ncol] = [s, d, z]
                    else:
                        temp[row][col] = [s, d, z]

        board = [t[:] for t in temp]
        # for b in board:
        #     print(b)
        # print()

    print(answer)


if __name__ == "__main__":
    solution()
