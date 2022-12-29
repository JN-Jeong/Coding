# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = 0
    while True:
        check = True
        for b in board:
            if sum(b) > 0:
                check = False
                break

        if check:
            return answer

        answer += 1
        temp = [[0] * (N) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                        cnt += 1

                if board[i][j] - cnt <= 0:
                    temp[i][j] = 0
                else:
                    temp[i][j] = board[i][j] - cnt

        board = temp


if __name__ == "__main__":
    print(solution())
