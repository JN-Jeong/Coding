# import copy


# def solution(grid):
#     answer = []
#     cycles = []

#     # 상 하 좌 우
#     dy = [-1, 1, 0, 0]
#     dx = [0, 0, -1, 1]

#     visited = []
#     for grid_row in grid:
#         v = []
#         for _ in grid_row:
#             v.append([0, 0, 0, 0])
#         visited.append(v)

#     row = len(grid)
#     col = len(grid[0])

#     def dfs(y, x, dir, cnt):
#         if visited[y][x][dir] == 1:
#             if visited not in cycles:
#                 answer.append(cnt)
#                 print("사이클", visited)

#             cycles.append(copy.deepcopy(visited))
#             print("cycles : ", cycles)
#             print("visited : ", visited)

#             return

#         if grid[y][x] == "L":  # L
#             # 상 -> 좌(+2), 하 -> 우(+2), 좌 -> 하(-1), 우 -> 상(+1)
#             if dir == 0 or dir == 1:
#                 n_dir = (dir + 2) % 4
#             elif dir == 2:
#                 n_dir = (dir - 1) % 4
#             elif dir == 3:
#                 n_dir = (dir + 1) % 4

#         elif grid[y][x] == "R":  # R
#             # 상 -> 우(-1), 하 -> 좌(+1), 좌 -> 상(+2), 우 -> 하(+2)
#             if dir == 0:
#                 n_dir = (dir - 1) % 4
#             elif dir == 1:
#                 n_dir = (dir + 1) % 4
#             elif dir == 2 or dir == 3:
#                 n_dir = (dir + 2) % 4

#         else:  # S
#             n_dir = dir
#             ny = y + dy[dir]
#             nx = x + dx[dir]

#         ny = (y + dy[n_dir]) % row
#         nx = (x + dx[n_dir]) % col

#         if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
#             print("@", y, x)
#             visited[y][x][dir] = 1
#             print(visited)
#             print(cycles)
#             dfs(ny, nx, n_dir, cnt + 1)
#             visited[y][x][dir] = 0

#     for d in range(4):
#         dfs(0, 0, d, 0)

#     return answer


def solution(grid):
    answer = []

    #     ↓  ←   ↑  →
    dy = (1, 0, -1, 0)
    dx = (0, -1, 0, 1)
    ly, lx = len(grid), len(grid[0])

    # 4방향 방문 기록 리스트 : y*x*4
    visited = [[[False] * 4 for _ in range(lx)] for _ in range(ly)]

    # 모든 좌표에 대하여 탐색
    for y in range(ly):
        for x in range(lx):

            # (y, x) 좌표에 대해 4방향 탐색
            for d in range(4):
                # 해당 좌표-방향 이 기존에 사용된 경우
                if visited[y][x][d]:
                    continue

                # 사용되지 않은 좌표-방향인 경우
                count = 0
                ny, nx = y, x
                # 빛을 이동 시켜가며 탐색
                while not visited[ny][nx][d]:
                    visited[ny][nx][d] = True
                    count += 1
                    if grid[ny][nx] == "S":  # S의 경우 방향 변경 X
                        pass
                    elif grid[ny][nx] == "L":  # L의 경우 반시계방향
                        d = (d - 1) % 4
                    elif grid[ny][nx] == "R":  # R의 경우 시계방향
                        d = (d + 1) % 4

                    # 좌표의 길이로 %연산을 하여 격자를 벗어난 경우에도 자리를 찾아가도록함.
                    ny = (ny + dy[d]) % ly
                    nx = (nx + dx[d]) % lx

                answer.append(count)
    answer = sorted(answer)  # 오름차순 정렬
    return answer


if __name__ == "__main__":
    grid = [["SL", "LR"], ["S"], ["R", "R"]]
    result = [[16], [1, 1, 1, 1], [4, 4]]

    for g in grid:
        print(solution(g))
        print()

cycles = [[[[1, 0, 0, 1]], [[0, 1, 1, 0]]], [[[1, 0, 0, 1]], [[0, 1, 1, 0]]], [[[1, 0, 0, 1]], [[0, 1, 1, 0]]], [[[1, 0, 0, 1]], [[0, 1, 1, 0]]]]
visited = [[[1, 0, 0, 1]], [[0, 1, 1, 0]]]

if cycles[0] == visited:
    print("chk")

if visited in cycles:
    print("###")
