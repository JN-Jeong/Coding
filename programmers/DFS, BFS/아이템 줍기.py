from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = make_board(rectangle)

    for b in board:
        print(b)

    characterX, characterY = characterX * 2, characterY * 2
    itemX, itemY = itemX * 2, itemY * 2
    print("board : ", len(board), len(board[0]))
    print("character : ", characterX, characterY)
    print("item : ", itemX, itemY)

    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = deque()
    q.append((characterX, characterY, 0))
    visited = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    visited[characterX][characterY] = 1

    while q:
        x, y, cnt = q.popleft()

        if x == itemX and y == itemY:
            print("######")
            return cnt // 2

        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            if is_not_wall(nx, ny, board) and is_side(nx, ny, board) and visited[nx][ny] == 0:
                print(nx, ny, cnt + 1)

                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1

    return answer

# board 생성
def make_board(rectangle: list):
    max_n = 0
    for rect in rectangle:
        max_n = max(max_n, max(rect) * 2)
    print(max_n)
    # max_n = 101

    board = [[0] * (max_n * 2) for _ in range(max_n * 2)]
    for x1, y1, x2, y2 in rectangle:
        x1, x2 = x1 * 2, x2 * 2
        y1, y2 = y1 * 2, y2 * 2
        for row in range(x1, x2 + 1):
            for col in range(y1, y2 + 1):
                board[row][col] = 1

    return board


# 지형의 변 부분인지 확인
# 변 부분이면 True를 반환
def is_side(x: int, y: int, board: list):
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))  # 8방향으로 확인

    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if is_not_wall(nx, ny, board) and board[x][y] == 1 and board[nx][ny] == 0:
            return True

    return False


# 보드의 범위를 벗어나는지 확인
# 보드의 범위를 벗어나지 않으면 True를 반환
def is_not_wall(row: int, col: int, board: list) -> bool:
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return True
    return False


rectangles = [
    [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]],
    # [[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]],
    # [[1, 1, 5, 7]],
    # [[2, 1, 7, 5], [6, 4, 10, 10]],
    # [[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]],
]
characterX = [1, 9, 1, 3, 1]
characterY = [3, 7, 1, 1, 4]
itemX = [7, 6, 4, 7, 6]
itemY = [8, 1, 7, 10, 3]
result = [17, 11, 9, 15, 10]

for rectangle, cX, cY, iX, iY in zip(rectangles, characterX, characterY, itemX, itemY):
    print(solution(rectangle, cX, cY, iX, iY))
    print()
