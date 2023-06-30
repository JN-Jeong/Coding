def solution():
    global answer
    answer = 0
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    shark = [N // 2, N // 2]
    n_zero = 0
    for b in board:
        n_zero += b.count(0)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def move():
        global answer
        step = 1
        turn = 2
        dy = [0, 1, 0, -1]
        dx = [-1, 0, 1, 0]
        d = 0

        idx = 0
        y, x = shark
        while True:
            if y == 0 and x == 0:
                break

            ny = y + dy[d]
            nx = x + dx[d]
            # print(y2, x2, d2, end=" / ")
            # print(board[y2][x2], end=" ")

            if board[y][x] == 0:
                if y == shark[0] and x == shark[1]:
                    pass
                else:
                    # print(y2, x2, "/", ny2, nx2)
                    # print(board[y2][x2], board[ny2][nx2])
                    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

            idx += 1
            if idx % step == 0:
                d = (d + 1) % 4
                if idx % turn == 0:
                    step += 1
                    turn += 1
            y = ny
            x = nx

    def boom():
        global answer
        step = 1
        turn = 2
        dy = [0, 1, 0, -1]
        dx = [-1, 0, 1, 0]
        d = 0

        idx = 0
        y, x = shark
        locs = []
        n_boom = 0
        while True:
            if y == 0 and x == 0:
                break

            temp = board[y][x]
            ny = y + dy[d]
            nx = x + dx[d]
            # print(y2, x2, d2, end=" / ")
            # print(board[y2][x2], end=" ")

            if board[ny][nx] == temp:
                if y == shark[0] and x == shark[1]:
                    pass
                else:
                    # print(y2, x2, "/", ny2, nx2)
                    # print(board[y2][x2], board[ny2][nx2])
                    locs.append([y, x])
            else:
                locs.append([y, x])
                if len(locs) >= 4:
                    for loc in locs:
                        ty, tx = loc
                        answer += board[ty][tx]
                        board[ty][tx] = 0
                        n_boom += 1
                locs = []

            idx += 1
            if idx % step == 0:
                d = (d + 1) % 4
                if idx % turn == 0:
                    step += 1
                    turn += 1
            y = ny
            x = nx

        return n_boom

    def change():
        step = 1
        turn = 2
        dy = [0, 1, 0, -1]
        dx = [-1, 0, 1, 0]
        d = 0

        idx = 0
        y, x = shark
        cnt = 0
        nums = []
        while True:
            if y == 0 and x == 0:
                break

            temp = board[y][x]
            ny = y + dy[d]
            nx = x + dx[d]

            if board[ny][nx] == temp:
                if temp == 0:
                    pass
                else:
                    cnt += 1
            else:
                if temp == 0:
                    pass
                else:
                    cnt += 1
                    nums.append(cnt)
                    nums.append(temp)
                    cnt = 0

            idx += 1
            if idx % step == 0:
                d = (d + 1) % 4
                if idx % turn == 0:
                    step += 1
                    turn += 1
            y = ny
            x = nx
        # print(nums)

        step = 1
        turn = 2
        d = 0

        i = 0
        idx = 0
        y, x = shark
        while True:
            if y == 0 and x == 0 or i >= len(nums):
                break

            temp = board[y][x]
            ny = y + dy[d]
            nx = x + dx[d]

            board[ny][nx] = nums[i]

            idx += 1
            if idx % step == 0:
                d = (d + 1) % 4
                if idx % turn == 0:
                    step += 1
                    turn += 1
            y = ny
            x = nx
            i += 1

    for _ in range(M):
        d, s = map(int, input().split())
        y, x = shark

        # 블리자드 마법 시전
        n_boom = 0
        for _ in range(s):
            y = y + dy[d - 1]
            x = x + dx[d - 1]

            if 0 <= y < N and 0 <= x < N:
                # answer += board[y][x]
                board[y][x] = 0
                n_boom += 1

        # print("#", answer)
        # for b in board:
        #     print(b)
        # print()

        # 구슬 이동
        # print(n_boom)
        for _ in range(n_boom):
            move()
        # print("##", answer)

        # 연속 구슬 폭발 + 구슬 이동
        while True:
            # 연속 구슬 폭발
            n_boom = boom()
            if n_boom == 0:
                break

            # for b in board:
            #     print(b)
            # print()

            # 구슬 이동
            for _ in range(n_boom):
                move()

            # for b in board:
            #     print(b)
            # print()
            # print("###", answer)

        # 구슬 변화
        # for b in board:
        #     print(b)
        # print()
        change()
        # for b in board:
        #     print(b)
        # print()

    # for b in board:
    #     print(b)
    # print()

    return answer


if __name__ == "__main__":
    print(solution())
