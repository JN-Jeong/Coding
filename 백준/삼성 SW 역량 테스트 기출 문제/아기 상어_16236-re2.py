from collections import deque


def solution():
    answer = 0
    N = int(input())
    global board
    board = [list(map(int, input().split())) for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if board[row][col] == 9:
                y = row
                x = col

    # 상좌우하
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    def bfs(s_row, s_col, shark):  # s_row, s_col : 아기 상어 위치, shark : 상어 크기
        global board
        q = deque()
        q.append([s_row, s_col, 0])
        visited = [[0] * N for _ in range(N)]
        visited[s_row][s_col] = 1

        result = []
        while q:
            row, col, count = q.popleft()

            for d in range(4):
                nrow = row + dy[d]
                ncol = col + dx[d]

                if 0 <= nrow < N and 0 <= ncol < N and board[nrow][ncol] <= shark and visited[nrow][ncol] == 0:
                    visited[nrow][ncol] = 1
                    q.append([nrow, ncol, count + 1])
                    if 0 < board[nrow][ncol] < shark:
                        result.append([nrow, ncol, count + 1])

        return sorted(result, key=lambda x: (-x[2], -x[0], -x[1]))

    shark = 2
    eat = 0
    while True:
        fish = bfs(y, x, shark)
        if len(fish) <= 0:
            break
        ny, nx, dis = fish.pop()

        answer += dis
        eat += 1
        board[y][x] = 0
        board[ny][nx] = 9
        y, x = ny, nx

        if eat == shark:
            shark += 1
            eat = 0

        print(len(fish), fish)
        # print(eat, shark, answer)
        # for b in board:
        #     print(b)
        # print()

    print(answer)


if __name__ == "__main__":
    solution()
