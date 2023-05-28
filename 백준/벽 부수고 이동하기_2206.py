from collections import deque


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input())) for _ in range(N)]

    q = deque()
    q.append([0, 0, 1])  # row, col, chance
    # 3차원으로 부수기 기회가 있을 때와 없을 때의 경로 길이를 각각 저장하도록 만듬
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # [row][col][0] : 부수기 기회 없을 때 방문 경로, [row][col][1] : 부수기 기회 있을 때 방문 경로
    visited[0][0] = [1, 1]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        row, col, chance = q.popleft()

        if row == N - 1 and col == M - 1:
            return visited[row][col][chance]

        for d in range(4):
            nrow = row + dy[d]
            ncol = col + dx[d]

            if 0 <= nrow < N and 0 <= ncol < M:
                if board[nrow][ncol] == 0 and visited[nrow][ncol][chance] == 0:
                    visited[nrow][ncol][chance] = visited[row][col][chance] + 1
                    q.append([nrow, ncol, chance])

                elif board[nrow][ncol] == 1 and chance == 1:
                    visited[nrow][ncol][0] = visited[row][col][chance] + 1
                    q.append([nrow, ncol, 0])

        # for v in visited:
        #     print(v)
        # print()

    return -1


if __name__ == "__main__":
    print(solution())
