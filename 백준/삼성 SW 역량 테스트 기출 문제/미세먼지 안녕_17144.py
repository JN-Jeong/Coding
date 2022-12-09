"""
1. 미세먼지 확산
- (r,c)에 인접한 네 방향으로 확산된다.
- 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
- 각각 확산되는 양은 A(r,c)/5이고 소수점은 버린다.
- (r,c)에 남은 미세먼지의 양은 A(r,c)-(A(r,c)/5) * (확산된 방향 개수)이다.

2. 공기청정기 작동
- 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
- 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
- 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

남아있는 미세먼지의 양?
"""


def solution():
    answer = 0
    R, C, T = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(R)]
    for a in board:
        print(a)

    for i in range(R):
        if board[i][0] == -1:
            machine = [[i, 1], [i + 1, 1]]  # 공기청정기 위, 아래 (column은 + 1해서 저장)
            break

    for i in range(T):
        board = spread(board)
        board = air_up(board, machine[0])
        board = air_down(board, machine[1])

    print()
    for b in board:
        print(b)

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                answer += board[i][j]

    return answer


def is_not_wall(board, row, col):  # 인덱스 범위 내 라면 True, 외 라면 False 반환
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return True
    return False


def spread(board):
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    temp_board = [[0] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0 and board[i][j] != -1:
                temp = 0
                for dx, dy in dir:
                    nx = i + dx
                    ny = j + dy
                    if is_not_wall(board, nx, ny) and board[nx][ny] != -1:
                        temp_board[nx][ny] += board[i][j] // 5
                        temp += board[i][j] // 5
                board[i][j] -= temp

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp_board[i][j]

    return board


def air_up(board, machine_loc):
    dir = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 우 상 좌 하 (반시계방향)
    dir_idx = 0
    temp = 0
    x, y = machine_loc

    while True:
        nx = x + dir[dir_idx][0]
        ny = y + dir[dir_idx][1]

        if x == machine_loc[0] and y == 0:  # 공기청정기로 돌아오면 종료
            break

        if not is_not_wall(board, nx, ny):  # 벽에 닿으면(범위를 벗어나면) 방향 전환
            dir_idx += 1
            continue

        board[x][y], temp = temp, board[x][y]
        x, y = nx, ny

    return board


def air_down(board, machine_loc):
    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상 (시계방향)
    dir_idx = 0
    temp = 0
    x, y = machine_loc

    while True:
        nx = x + dir[dir_idx][0]
        ny = y + dir[dir_idx][1]

        if x == machine_loc[0] and y == 0:  # 공기청정기로 돌아오면 종료
            break

        if not is_not_wall(board, nx, ny):  # 벽에 닿으면(범위를 벗어나면) 방향 전환
            dir_idx += 1
            continue

        board[x][y], temp = temp, board[x][y]
        x, y = nx, ny

    return board


if __name__ == "__main__":
    print(solution())
