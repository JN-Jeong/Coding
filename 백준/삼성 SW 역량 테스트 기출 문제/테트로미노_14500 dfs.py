def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    global answer
    answer = 0
    max_val = max(map(max, board))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[0] * M for _ in range(N)]

    def dfs(row, col, cnt, total):
        global answer
        if answer >= total + max_val * (4 - cnt):
            return

        if cnt == 4:
            answer = max(answer, total)
            return

        for d in range(4):
            nrow = row + dy[d]
            ncol = col + dx[d]

            if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] == 0:
                visited[nrow][ncol] = 1
                dfs(nrow, ncol, cnt + 1, total + board[nrow][ncol])
                visited[nrow][ncol] = 0
                if cnt == 2:
                    visited[nrow][ncol] = 1
                    dfs(row, col, cnt + 1, total + board[nrow][ncol])
                    visited[nrow][ncol] = 0

    for r in range(N):
        for c in range(M):
            visited[r][c] = 1
            dfs(r, c, 1, board[r][c])
            visited[r][c] = 0

    print(answer)


if __name__ == "__main__":
    solution()
