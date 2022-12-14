"""
순번대로 움직이는 것이 아니라 모든 상어가 동시에 움직인다
"""


def solve():
    def smell_update():
        for i in range(N):
            for j in range(N):
                if smell_board[i][j][1] > 0:  # 냄새 지속시간 갱신
                    smell_board[i][j][1] -= 1
                if shark_board[i][j]:  # 냄새 남김
                    smell_board[i][j] = [shark_board[i][j], k]

    def shark_move():
        n_shark_board = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if shark_board[i][j]:
                    shark_num = shark_board[i][j]
                    move_check = False
                    # 1. 냄새 없는 곳 탐색
                    for dir in sharks_dir_prior[shark_num - 1][sharks_dir[shark_num - 1] - 1]:
                        print("@", shark_num, dir)
                        nx = i + dx[dir - 1]
                        ny = j + dy[dir - 1]

                        if 0 <= nx < N and 0 <= ny < N and smell_board[nx][ny][1] == 0:
                            sharks_dir[shark_num - 1] = dir  # 방향 갱신

                            # 이동한 위치에 다른 상어가 없다면 상어 이동
                            # 상어가 있으면 번호가 큰 상어가 잡아먹힘
                            if n_shark_board[nx][ny] == 0:
                                n_shark_board[nx][ny] = shark_num
                            else:
                                n_shark_board[nx][ny] = min(shark_num, n_shark_board[nx][ny])

                            move_check = True
                            for b in n_shark_board:
                                print(b)
                            print()
                            break

                    if move_check:
                        continue

                    # 2. 본인 냄새 있는 곳 탐색
                    for dir in sharks_dir_prior[shark_num - 1][sharks_dir[shark_num - 1] - 1]:
                        # print("#", shark_num, dir)
                        nx = i + dx[dir - 1]
                        ny = j + dy[dir - 1]

                        if 0 <= nx < N and 0 <= ny < N and smell_board[nx][ny][0] == shark_num:
                            sharks_dir[shark_num - 1] = dir  # 방향 갱신

                            n_shark_board[nx][ny] = shark_num

                            move_check = True
                            for b in n_shark_board:
                                print(b)
                            print()
                            break
        return n_shark_board

    answer = 0
    N, M, k = map(int, input().split())
    shark_board = [list(map(int, input().split())) for _ in range(N)]  # 상어 위치 board
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    sharks_dir = list(map(int, input().split()))  # 현재 상어의 방향
    sharks_dir_prior = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]  # 상어의 방향 우선순위
    smell_board = [[[0, 0]] * N for _ in range(N)]  # 냄새 위치 board (상어 번호, 냄새 지속시간)

    # print("sharks dir : ", sharks_dir)
    # print("sharks dir prior : ", sharks_dir_prior)
    # for b in smell_board:
    #     print(b)
    # print()

    while True:
        smell_update()
        for b in smell_board:
            print(b)
        print()
        shark_board = shark_move()

        answer += 1
        check = 0
        for i in range(N):
            for j in range(N):
                if shark_board[i][j] > 1:
                    check += shark_board[i][j]

        if check == 0:
            break

        if answer >= 1000:
            return -1

        # for b in board:
        #     print(b)
        # print()

    return answer


if __name__ == "__main__":
    print(solve())
