"""
15686. 치킨 배달
"""
from collections import deque


def solution():
    global answer
    answer = float("inf")
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    chicken = []
    homes = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                homes.append([i, j])
            if board[i][j] == 2:
                chicken.append([i, j])

    def dfs(idx, cnt):
        global answer
        if cnt == M:
            temp = 0
            for i, j in homes:
                temp += min_path(i, j)
            answer = min(answer, temp)
            return

        for i in range(idx, K):
            remains.append(chicken[i])
            dfs(i + 1, cnt + 1)
            remains.pop()

    def min_path(row, col):
        dis = float("inf")

        for i, j in remains:
            dis = min(dis, abs(row - i) + abs(col - j))

        return dis

    remains = deque()
    K = len(chicken)
    for i in range(K):
        dfs(i, 0)

    return answer


if __name__ == "__main__":
    print(solution())
