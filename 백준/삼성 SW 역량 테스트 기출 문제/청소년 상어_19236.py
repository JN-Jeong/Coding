import copy


def solution():
    board = [[] for _ in range(4)]

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    for i in range(4):
        temp = list(map(int, input().split()))
        fish = []
        for j in range(4):
            # 물고기 번호, 방향 저장
            fish.append([temp[2 * j], temp[2 * j + 1] - 1])
        board[i] = fish

    global answer
    answer = 0

    def dfs(shark_x, shark_y, score, board):
        global answer
        score += board[shark_x][shark_y][0]  # 상어 식사
        answer = max(answer, score)
        board[shark_x][shark_y][0] = 0  # 물고기 소화

        # 물고기 이동
        for f in range(1, 17):
            fish_x, fish_y = -1, -1
            # 완전 탐색으로 순서대로 물고기 이동시킴
            for x in range(4):
                for y in range(4):
                    if board[x][y][0] == f:
                        fish_x, fish_y = x, y
                        break
            if fish_x == -1 and fish_y == -1:  # 해당 번호의 물고기가 소화되었으면 continue
                continue
            fish_dir = board[fish_x][fish_y][1]

            # 방향 전환
            for i in range(8):
                nd = (fish_dir + i) % 8
                nx = fish_x + dx[nd]
                ny = fish_y + dy[nd]
                if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == shark_x and ny == shark_y):
                    continue
                board[fish_x][fish_y][1] = nd  # 새로운 이동 방향 갱신
                board[fish_x][fish_y], board[nx][ny] = board[nx][ny], board[fish_x][fish_y]  # 이동할 위치의 물고기와 위치 변경
                break

        # 상어 이동
        shark_dir = board[shark_x][shark_y][1]
        for i in range(1, 4):  # 최대 3칸 이동
            nx = shark_x + dx[shark_dir] * i
            ny = shark_y + dy[shark_dir] * i
            # 물고기가 있는 칸으로 이동, 이동할 수 있는 칸에 물고기가 없다면 이동하지 않아서 종료
            if (0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
                dfs(nx, ny, score, copy.deepcopy(board))

        print(shark_x, shark_y, shark_dir)
        for b in board:
            print(b)
        print()

    dfs(0, 0, 0, board)
    return answer


if __name__ == "__main__":
    print(solution())
