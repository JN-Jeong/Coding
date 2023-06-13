def solution():
    board = [list(map(int, input().split())) for _ in range(19)]

    # 4방향 (→ ↓ ↘ ↗)
    # 가장 왼쪽에 있는 바둑알(연속된 다섯 개의 바둑알이 세로로 놓인 경우, 그 중 가장 위에 있는 것)의 위치를 반환하기 위해 4방향만 탐색
    dy = [0, 1, 1, -1]
    dx = [1, 0, 1, 1]

    for y in range(len(board)):
        for x in range(len(board[0])):
            color = board[y][x]
            if color:
                for i in range(4):
                    cnt = 1
                    ny = y + dy[i]
                    nx = x + dx[i]
                    while 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == color:
                        cnt += 1
                        if cnt == 5:
                            if 0 <= ny + dy[i] < len(board) and 0 <= nx + dx[i] < len(board[0]) and board[ny + dy[i]][nx + dx[i]] == color:
                                break
                            if 0 <= y - dy[i] < len(board) and 0 <= x - dx[i] < len(board[0]) and board[y - dy[i]][x - dx[i]] == color:
                                break

                            print(color)
                            print(y + 1, x + 1)
                            return

                        ny += dy[i]
                        nx += dx[i]

    print(0)


if __name__ == "__main__":
    solution()
