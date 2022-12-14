def solve():
    answer = 0
    N, M, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    sharks_dir = list(map(int, input().split()))  # 현재 상어의 방향
    sharks_dir_prior = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]  # 상어의 방향 우선순위

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                # board[i][j] = {"shark": board[i][j], "smell": [board[i][j], k]}
                board[i][j] = {"shark": board[i][j], "smell": [0, 0]}  # smell : [상어 번호, 냄새 지속시간]
            else:
                board[i][j] = {"shark": 0, "smell": [0, 0]}  # smell : [상어 번호, 냄새 지속시간]

    # print("sharks dir : ", sharks_dir)
    # print("sharks dir prior : ", sharks_dir_prior)
    # for b in board:
    #     print(b)
    # print()

    while True:
        for i in range(N):
            for j in range(N):
                if board[i][j]["smell"][1] > 0:  # 냄새 지속시간 갱신
                    board[i][j]["smell"][1] -= 1
                if board[i][j]["smell"][1] == 0 and board[i][j]["shark"] == 0:  # 냄새 지우기
                    board[i][j] = {"shark": 0, "smell": [0, 0]}

        for shark_num in range(1, M + 1):
            move_check = False
            for i in range(N):
                for j in range(N):
                    if board[i][j]["shark"] == shark_num:
                        # 1. 냄새 없는 곳 탐색
                        for dir in sharks_dir_prior[shark_num - 1][sharks_dir[shark_num - 1] - 1]:
                            print(shark_num, dir)
                            nx = i + dx[dir - 1]
                            ny = j + dy[dir - 1]

                            if 0 <= nx < N and 0 <= ny < N and board[nx][ny]["smell"][0] == 0:
                                board[i][j] = {"shark": 0, "smell": [shark_num, k]}  # 냄새 남김
                                sharks_dir[shark_num - 1] = dir  # 방향 갱신

                                # 이동한 위치에 다른 상어가 없다면 상어 이동
                                # 우선 순위가 있기 때문에 나중에 움직인 상어가 이동한 위치에 상어가 있으면 잡아먹혀서 없어짐
                                if board[nx][ny]["shark"] == 0:
                                    # board[nx][ny] = {"shark": shark_num, "smell": [0, 0]}
                                    board[nx][ny]["shark"] = shark_num

                                move_check = True
                                for b in board:
                                    print(b)
                                print()
                                break

                        if move_check == False:  # 이동하지 않았다면
                            # 2. 본인 냄새 있는 곳 탐색
                            for dir in sharks_dir_prior[shark_num - 1][sharks_dir[shark_num - 1] - 1]:
                                print(shark_num, dir)
                                nx = i + dx[dir - 1]
                                ny = j + dy[dir - 1]

                                if 0 <= nx < N and 0 <= ny < N and board[nx][ny]["smell"][0] == shark_num:
                                    board[i][j] = {"shark": 0, "smell": [shark_num, k]}  # 냄새 남김
                                    sharks_dir[shark_num - 1] = dir  # 방향 갱신

                                    # 이동한 위치에 다른 상어가 없다면 상어 이동
                                    # 우선 순위가 있기 때문에 나중에 움직인 상어가 이동한 위치에 상어가 있으면 잡아먹혀서 없어짐
                                    if board[nx][ny]["shark"] == 0:
                                        # board[nx][ny] = {"shark": shark_num, "smell": [0, 0]}
                                        board[nx][ny]["shark"] = shark_num

                                    move_check = True
                                    for b in board:
                                        print(b)
                                    print()
                                    break

                    if move_check:
                        break
                if move_check:
                    break
        answer += 1
        check = 0
        for i in range(N):
            for j in range(N):
                if board[i][j]["shark"] > 1:
                    check += board[i][j]["shark"]

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
