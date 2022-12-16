def rot_90(tornado):
    return list(reversed(list(map(list, zip(*tornado)))))


def sands():
    sand_loc = [
        [0, 0, 0.02, 0, 0],
        [0, 0.10, 0.07, 0.01, 0],
        [0.05, 0, 0, 0, 0],
        [0, 0.10, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0],
    ]

    sand_locs = []
    sand_locs.append(sand_loc)
    sand_locs.append(rot_90(sand_loc))
    sand_locs.append(rot_90(rot_90(sand_loc)))
    sand_locs.append(rot_90(rot_90(rot_90(sand_loc))))

    return sand_locs


def solve():
    answer = 0
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # for b in board:
    #     print(b)

    mid = N // 2

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    x = y = mid
    # print(x, y)

    """토네이도 이동을 위한 변수"""
    repeat = 0  # 현재 방향 반복
    turn = 2  # 방향 회전
    dir = 0  # 현재 토네이도 진행 방향
    alpahs = [
        [2, 1],
        [3, 2],
        [2, 3],
        [1, 2],
    ]

    """모래 날림 비율"""
    sand_ratios = sands()
    sand_ratio = sand_ratios[0]

    while True:
        if x == 0 and y == 0:
            break

        """토네이도 이동"""
        x += dx[dir]
        y += dy[dir]
        repeat += 1  # 같은 방향 이동 횟수
        sand = board[x][y]  # 날릴 모래
        board[x][y] = 0
        left = sand  # 남은 모래

        """모래 날림"""
        for i in range(5):
            for j in range(5):
                now_sand = int(sand * sand_ratio[i][j])
                left -= now_sand

                row = x + i - 2
                col = y + j - 2
                if 0 <= row < N and 0 <= col < N:
                    board[row][col] += now_sand
                else:
                    answer += now_sand

        """알파 위치에 남은 모래 두기"""
        row = x + alpahs[dir][0] - 2
        col = y + alpahs[dir][1] - 2
        if 0 <= row < N and 0 <= col < N:
            board[row][col] += left
        else:
            answer += left

        """토네이도 방향 갱신"""
        if repeat == turn // 2 or repeat == turn:
            dir = (dir + 1) % 4
            sand_ratio = sand_ratios[dir]
            if repeat == turn:
                repeat = 0
                turn += 2

    return answer


if __name__ == "__main__":
    print(solve())
