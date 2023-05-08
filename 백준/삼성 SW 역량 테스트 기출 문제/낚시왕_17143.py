def solution():
    R, C, M = map(int, input().split())
    board = [[[] for _ in range(C)] for _ in range(R)]
    for _ in range(M):
        r, c, speed, d, z = map(int, input().split())
        board[r - 1][c - 1] = [speed, d - 1, z]  # 속력, 방향, 크기

    answer = 0

    def get_next_loc(row, col, speed, d):
        if d == 0 or d == 1:  # row
            cycle = R * 2 - 2
            if d == 0:
                speed += 2 * (R - 1) - row
            else:
                speed += row

            speed %= cycle
            if speed >= R:
                return (2 * R - 2 - speed, col, 0)
            return (speed, col, 1)

        else:  # col
            cycle = C * 2 - 2
            if d == 3:
                speed += 2 * (C - 1) - col
            else:
                speed += col

            speed %= cycle
            if speed >= C:
                return (row, 2 * C - 2 - speed, 3)
            return (row, speed, 2)

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
                    speed, d, z = board[row][col]

                    # 상어 위치
                    nrow, ncol, d = get_next_loc(row, col, speed, d)
                    print(nrow, ncol, speed, d)

                    if temp[nrow][ncol]:
                        temp_s, temp_d, temp_z = temp[nrow][ncol]
                        if temp_z < z:
                            temp[nrow][ncol] = [speed, d, z]
                    else:
                        temp[nrow][ncol] = [speed, d, z]

        board = [t[:] for t in temp]
        for b in board:
            print(b)
        print()

    print(answer)


if __name__ == "__main__":
    solution()
