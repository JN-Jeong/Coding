"""
https://softeer.ai/practice/6275
[HSAT 1회 정기 코딩 인증평가 기출] 로봇이 지나간 경로
"""

import sys
from collections import deque


def solution():
    H, W = map(int, input().split())
    directs = ["^", "<", "v", ">"]

    board = [list(input()) for _ in range(H)]
    # for b in board:
    #     print(b)
    # print()

    # 상좌하우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    def isin(y, x):
        if 0 <= y < H and 0 <= x < W:
            return True
        return False

    def findStart():
        for y in range(H):
            for x in range(W):
                if board[y][x] == "#":
                    cnt = 0
                    nd = 0
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if isin(ny, nx) and board[ny][nx] == "#":
                            cnt += 1
                            nd = d
                    if cnt == 1:
                        return [y, x, nd]

    y, x, direction = findStart()
    q = deque()
    q.append([y, x, direction])
    print(y + 1, x + 1)
    print(directs[direction])
    board[y][x] = "."

    while q:
        y, x, direction = q.popleft()

        for d in [0, 1, -1]:
            nd = (direction + d) % 4
            ny = y + dy[nd]
            nx = x + dx[nd]

            if isin(ny, nx) and board[ny][nx] == "#":
                board[ny][nx] = "."
                ny += dy[nd]
                nx += dx[nd]
                board[ny][nx] = "."
                q.append([ny, nx, nd])
                if d == 1:
                    print("L", end="")
                elif d == -1:
                    print("R", end="")
                print("A", end="")


if __name__ == "__main__":
    solution()
