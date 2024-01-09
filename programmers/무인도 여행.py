"""
무인도 여행
"""
from collections import deque


def solution(maps):
    answer = []

    N = len(maps)
    M = len(maps[0])
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    visited = [[0] * M for _ in range(N)]

    def isin(y, x):
        if 0 <= y < N and 0 <= x < M:
            return True
        return False

    for i in range(N):
        for j in range(M):
            if maps[i][j] != "X" and visited[i][j] == 0:
                q = deque()
                q.append([i, j])
                visited[i][j] = 1

                total = 0
                while q:
                    y, x = q.popleft()
                    total += int(maps[y][x])
                    print("@", y, x, total)

                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if (
                            isin(ny, nx)
                            and maps[ny][nx] != "X"
                            and visited[ny][nx] == 0
                        ):
                            q.append([ny, nx])
                            visited[ny][nx] = 1

                answer.append(total)

    if answer:
        return sorted(answer)
    return [-1]


if __name__ == "__main__":
    maps = [["X591X", "X1X5X", "X231X", "1XXX1"], ["XXX", "XXX", "XXX"]]
    answer = [[1, 1, 27], [-1]]

    for i, data in enumerate(maps):
        gem = data
        print(f"#{i}", solution(gem))
