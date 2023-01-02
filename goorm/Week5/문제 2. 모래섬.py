# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import copy
from collections import deque


def solution():
    answer = 0
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0] * M for _ in range(N)]

    while True:
        cnt = 0
        visited = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0 or visited[i][j] == 1:
                    continue
                visited[i][j] = 1
                cnt += 1
                q = deque()
                q.append([i, j])
                while q:
                    y, x = q.popleft()
                    for d in range(4):
                        nrow = y + dy[d]
                        ncol = x + dx[d]
                        if 0 <= nrow < len(board) and 0 <= ncol < len(board[0]) and board[nrow][ncol] == 1 and visited[nrow][ncol] == 0:
                            visited[nrow][ncol] = 1
                            q.append([nrow, ncol])

        if cnt > 1:
            # print("@@@@@@@")
            return answer

        if cnt == 0:
            return -1

        board = water(board)
        # for b in board:
        #     print(b)
        # print()
        answer += 1


def water(board):
    temp = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                for d in range(4):
                    nrow = i + dy[d]
                    ncol = j + dx[d]
                    if 0 <= nrow < len(board) and 0 <= ncol < len(board[0]):
                        temp[nrow][ncol] = 0

    return temp


if __name__ == "__main__":
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    print(solution())
