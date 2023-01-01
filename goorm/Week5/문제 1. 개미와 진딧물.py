# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    answer = 0
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ants = []
    bugs = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                ants.append([i, j])
            if board[i][j] == 2:
                bugs.append([i, j])

    for ay, ax in ants:
        for by, bx in bugs:
            if abs(ay - by) + abs(ax - bx) <= M:
                answer += 1
                break

    return answer


if __name__ == "__main__":
    print(solution())
