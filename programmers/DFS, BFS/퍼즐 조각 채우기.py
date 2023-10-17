"""
game_boards의 빈 칸을 찾고 해당 빈 칸의 도형과 같은 도형을 tables에서 하나씩 찾도록 해보자

시간 초과 개선 : visited를 통해 bfs 탐색 횟수를 줄임
"""


from collections import deque


def solution(game_board, table):
    answer = 0
    shapes = []
    # print_board(game_board)
    # print_board(table)

    shape_size = []
    visited = [[0] * len(game_board[0]) for _ in range(len(game_board))]
    for row in range(len(table)):
        shape = []
        for col in range(len(table[0])):
            if table[row][col] and visited[row][col] == 0:
                shape_idx = bfs(row, col, table, visited)
                shape = idx_to_shape(shape_idx)
                shapes.append(shape)
                shape_size.append(len(shape_idx))

    for idx, shape in enumerate(shapes):
        for _ in range(4):
            # shape = np.rot90(shape)  # 반시계 방향으로 90도 회전
            shape = rotate(shape)
            if is_match(shape, game_board):
                answer += shape_size[idx]
                # print_shape(shape)
                # print_board(game_board)
                break

    # print("shapes : ", shapes)
    # print_shapes(shapes)

    return answer


# 도형 탐색
def bfs(i: int, j: int, table: list, visited: list):
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = deque()
    q.append((i, j))
    shape = []
    visited[i][j] = 1
    while q:
        row, col = q.popleft()

        if table[row][col]:
            # print(row, col)
            shape.append((row, col))
            table[row][col] = 0

        for dx, dy in dir:
            nrow, ncol = row + dx, col + dy

            if is_not_wall(nrow, ncol, table) and table[nrow][ncol] == 1 and visited[nrow][ncol] == 0:
                q.append((nrow, ncol))
                visited[nrow][ncol] = 1

    # print_board(table)

    return shape


def print_board(board: list):
    for b in board:
        print(b)
    print()


def print_shapes(shapes: list):
    for shape in shapes:
        for s in shape:
            print(s)
        print()


def print_shape(shape: list):
    for s in shape:
        print(s)
    print()


# 벽이면 False, 벽이 없는 자리이면 True를 반환
def is_not_wall(row: int, col: int, board: list) -> bool:
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return True
    return False


# 도형을 회전시키면서 보드에 맞는지 확인해야함
# 도형을 회전시키기 위해 인덱스로 저장해둔 도형을 리스트로 만들어줌
def idx_to_shape(shape: list):
    max_row, min_row = 0, float("inf")
    max_col, min_col = 0, float("inf")

    for dx, dy in shape:
        max_row, min_row = max(max_row, dx), min(min_row, dx)
        max_col, min_col = max(max_col, dy), min(min_col, dy)

    len_row = max_row - min_row + 1
    len_col = max_col - min_col + 1
    temp = [[0] * (len_col) for _ in range(len_row)]

    for dx, dy in shape:
        x = dx - min_row
        y = dy - min_col
        temp[x][y] = 1

    return temp


# 90도 회전
def rotate(shape: list):
    row = len(shape)
    col = len(shape[0])
    result = [[0] * row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            result[c][row - 1 - r] = shape[r][c]

    return result


# 도형을 넣을 수 있는지 확인
# 넣을 수 있다면 True를 반환하고 도형을 넣은 자리를 1로 채움
# 넣을 수 없다면 False를 반환하고 도형을 넣지 않음 (0으로 복원)
def is_match(shape: list, board: list):
    board_row = len(board)
    board_col = len(board[0])
    shape_row = len(shape)
    shape_col = len(shape[0])

    for i in range(board_row - shape_row + 1):
        for j in range(board_col - shape_col + 1):
            match_flag = True
            for x in range(shape_row):
                for y in range(shape_col):
                    board[i + x][j + y] += shape[x][y]
                    if board[i + x][j + y] != 1:
                        match_flag = False

            # print("# : ", i, j)
            if is_blank(i, j, shape, board):
                # print("blank")
                # print_shape(shape)
                match_flag = False

            if match_flag:
                # print("match")
                # print_shape(shape)
                # print_board(board)
                return True
            else:  # 0으로 복원
                for x in range(shape_row):
                    for y in range(shape_col):
                        board[i + x][j + y] -= shape[x][y]

    return False


# 도형을 넣었을 때 인접한 곳에 빈 칸이 있는지 확인
# 빈 칸이 있다면 True를 반환
def is_blank(i: int, j: int, shape: list, board: list):
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

    shape_row = len(shape)
    shape_col = len(shape[0])
    # print("shape : ", shape_row, shape_col)
    for x in range(shape_row):
        for y in range(shape_col):
            if shape[x][y] == 1:  # 도형 형태의 인접 부분만 확인 (범위 리스트 전체가 도형이 아님)
                for dx, dy in dir:
                    nx, ny = x + dx + i, y + dy + j
                    if is_not_wall(nx, ny, board) and board[nx][ny] != 1:
                        return True

    return False


game_boards = [
    [
        [1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0],
    ],
    [[0, 0, 0], [1, 1, 0], [1, 1, 1]],
]
tables = [
    [
        [1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
    ],
    [[1, 1, 1], [1, 0, 0], [0, 0, 0]],
]
result = [14, 0]

for board, table in zip(game_boards, tables):
    print(solution(board, table))
