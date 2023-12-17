"""
https://softeer.ai/practice/6246
[HSAT 7회 정기 코딩 인증평가 기출] 순서대로 방문하기
"""

import sys


def solution():
    global answer
    answer = 0
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    locs = []
    for _ in range(m):
        y, x = map(int, input().split())
        y -= 1
        x -= 1
        locs.append([y, x])

    # 상좌하우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    def isin(y, x):
        if 0 <= y < n and 0 <= x < n:
            return True
        return False

    def check(path):
        idx = 0
        for i in range(len(path)):
            if locs[idx] == path[i]:
                idx += 1

        if idx == len(locs):
            return True
        return False

    def dfs(y, x, visited, path):
        global answer
        path.append([y, x])
        if y == locs[-1][0] and x == locs[-1][1]:
            if check(path):
                answer += 1
            return

        visited[y][x] = 1

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if isin(ny, nx) and visited[ny][nx] == 0 and board[ny][nx] != 1:
                visited[ny][nx] = 1
                # for v in visited:
                #     print(v)
                # print("@", path)
                # print()
                dfs(ny, nx, visited, path[:])
                visited[ny][nx] = 0

    visited = [[0] * n for _ in range(n)]
    dfs(locs[0][0], locs[0][1], visited, [])
    return answer


if __name__ == "__main__":
    print(solution())
