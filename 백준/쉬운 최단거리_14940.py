"""
14940. 쉬운 최단거리
"""
from collections import deque


def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    zeros = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                target = [i, j]
            elif board[i][j] == 0:
                zeros.append([i, j])

    q = deque()
    q.append([target[0], target[1], 0])

    def isin(y, x):
        if 0 <= y < n and 0 <= x < m:
            return True
        return False

    while q:
        y, x, cnt = q.popleft()
        visited[y][x] = cnt

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if isin(ny, nx) and visited[ny][nx] == -1:
                if board[ny][nx]:
                    q.append([ny, nx, cnt + 1])
                    visited[ny][nx] = cnt + 1

    visited[target[0]][target[1]] = 0
    for zero in zeros:
        y, x = zero
        visited[y][x] = 0

    for v in visited:
        print(" ".join(map(str, v)))


if __name__ == "__main__":
    solution()
