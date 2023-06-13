def solution():
    board = [list(map(int, input().split())) for _ in range(19)]

    # 8방향
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    visited = [[0] * len(board[0]) for _ in range(len(board))]

    for y in range(len(board)):
        for x in range(len(board[0])):
            color = board[y][x]
            if color:
                for i in range(8):
                    cnt = 0

                    for j in range(6):
                        ny = y + dy[i] * j
                        nx = x + dx[i] * j
                        if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == color:
                            # print(f"{y} {x} / {ny} {nx} / {color} / {i}")
                            cnt += 1

                    if cnt == 6:
                        for j in range(6):
                            ny = y + dy[i] * j
                            nx = x + dx[i] * j
                            visited[ny][nx] = 1

                    if cnt == 5 and 0 <= y < len(board) and 0 <= x < len(board[0]) and visited[y][x] == 0:
                        print(color)
                        if i == 0 or i == 6:
                            ny = y + dy[i] * 4
                            nx = x + dx[i] * 4
                            print(ny + 1, nx + 1)
                        elif i == 1:
                            ny = y + dy[i] * 4
                            print(ny + 1, x + 1)
                        else:
                            print(y + 1, x + 1)
                        return

    print(0)


if __name__ == "__main__":
    solution()
