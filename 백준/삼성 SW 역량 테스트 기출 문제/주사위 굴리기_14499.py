from collections import deque


def solution():
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    commands = list(map(int, input().split()))

    dice = {}
    for i in range(1, 7):
        dice[i] = 0

    # 동서북남, 우좌상하
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    q1 = deque([1, 2, 6, 5])  # 북, 남 이동
    q2 = deque([1, 3, 6, 4])  # 동, 서 이동

    for c in commands:
        nx = x + dx[c - 1]
        ny = y + dy[c - 1]

        if 0 <= nx < N and 0 <= ny < M:
            # 주사위 index 갱신
            if c == 1:  # 동
                q2.rotate(1)
                q1[0], q1[2] = q2[0], q2[2]
            elif c == 2:  # 서
                q2.rotate(-1)
                q1[0], q1[2] = q2[0], q2[2]
            elif c == 3:  # 북
                q1.rotate(1)
                q2[0], q2[2] = q1[0], q1[2]
            elif c == 4:  # 남
                q1.rotate(-1)
                q2[0], q2[2] = q1[0], q1[2]

            # print(q1, q2)

            if board[nx][ny] == 0:
                board[nx][ny] = dice[q1[2]]
            else:
                dice[q1[2]] = board[nx][ny]
                dice[q2[2]] = board[nx][ny]
                board[nx][ny] = 0

            print(dice[q1[0]])
            x, y = nx, ny


if __name__ == "__main__":
    solution()

"""
남쪽으로 굴렸을 때: 1 -> 2 -> 6 -> 5
북쪽으로 굴렸을 때: 1 -> 5 -> 6 -> 2
동쪽으로 굴렸을 때: 1 -> 4 -> 6 -> 3
서쪽으로 굴렸을 때: 1 -> 3 -> 6 -> 4

남1, 동1: 1 -> 2 -> 4
남1, 서1: 1 -> 2 -> 3 
북1, 동1: 1 -> 5 -> 4
북1, 서1: 1 -> 5 -> 3
남2, 동1: 1 -> 2 -> 6 -> 4
남2, 동1, 남1: 1 -> 2 -> 6 -> 4 -> 5
남2, 동1, 남1, 동1: 1 -> 2 -> 6 -> 4 -> 5 -> 1
남2, 동1, 남1, 서1: 1 -> 2 -> 6 -> 4 -> 5 -> 6
"""
