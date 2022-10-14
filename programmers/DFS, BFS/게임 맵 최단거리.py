from collections import deque


# 벽이면 False, 벽이 없는 자리이면 True를 반환
def is_not_wall(row: int, col: int, map: list) -> bool:
    if 0 <= row < len(map) and 0 <= col < len(map[0]) and map[row][col]:
        return True
    return False


def solution(maps):
    answer = float("inf")

    # 상하좌우 탐색
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = deque()
    q.append(((0, 0), 1))  # (0, 0) : 처음 시작 위치, 1 : 이동 횟수
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    while q:
        (row, col), cnt = q.popleft()
        if row == len(maps) - 1 and col == len(maps[0]) - 1:
            return cnt

        for d in dir:
            nrow, ncol = row + d[0], col + d[1]
            if is_not_wall(nrow, ncol, maps) and visited[nrow][ncol] != 1:
                q.append(((nrow, ncol), cnt + 1))
                visited[nrow][ncol] = 1
                print(visited)

    if answer == float("inf"):
        return -1
    return answer


maps = [
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
    ],
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
    ],
]
answer = [11, -1]

for map in maps:
    print(solution(map))
