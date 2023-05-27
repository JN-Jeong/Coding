from copy import deepcopy


def solution():
    board = [[] for _ in range(4)]
    # 8방향
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]

    for i in range(4):
        temp = list(map(int, input().split()))
        fish = []
        for j in range(4):
            fish.append([temp[2 * j], temp[2 * j + 1] - 1])
        board[i] = fish

    for b in board:
        print(b)

    global answer
    answer = 0

    def dfs(shark_y, shark_x, score, board):  # 상어 위치, 물고기 번호 합, board
        global answer
        score += board[shark_y][shark_x][0]
        answer = max(answer, score)
        board[shark_y][shark_x][0] = 0

        # 물고기 이동
        for f in range(1, 17):
            fish_y, fish_x = -1, -1
            for y in range(4):
                for x in range(4):
                    if board[y][x][0] == f:
                        fish_y, fish_x = y, x
                        break
            if fish_y == -1 and fish_x == -1:
                continue
            fish_dir = board[fish_y][fish_x][1]

            for i in range(8):
                nd = (fish_dir + i) % 8
                ny = fish_y + dy[nd]
                nx = fish_x + dx[nd]
                if not (0 <= ny < 4 and 0 <= nx < 4) or (ny == shark_y and nx == shark_x):
                    continue
                board[fish_y][fish_x][1] = nd
                board[fish_y][fish_x], board[ny][nx] = board[ny][nx], board[fish_y][fish_x]
                break

        # 상어 이동
        shark_dir = board[shark_y][shark_x][1]
        for i in range(1, 4):
            ny = shark_y + dy[shark_dir] * i
            nx = shark_x + dx[shark_dir] * i
            if (0 <= ny < 4 and 0 <= nx < 4) and board[ny][nx][0] > 0:
                dfs(ny, nx, score, deepcopy(board))

    dfs(0, 0, 0, board)
    print(answer)


if __name__ == "__main__":
    solution()
