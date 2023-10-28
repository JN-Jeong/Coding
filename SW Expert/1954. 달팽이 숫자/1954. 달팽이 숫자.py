"""
SW Expert Academy : 1954. 달팽이 숫자
"""
from collections import deque


def solve():
    input_ = int(input())

    board = [[0] * input_ for _ in range(input_)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    y = 0
    x = 0
    d = 0
    for num in range(1, input_**2 + 1):
        board[y][x] = str(num)

        ny = y + dy[d]
        nx = x + dx[d]

        if (ny < 0 or ny >= input_) or (nx < 0 or nx >= input_) or board[ny][nx] != 0:
            d = (d + 1) % 4
            ny = y + dy[d]
            nx = x + dx[d]

        y = ny
        x = nx

    for b in board:
        print(" ".join(b))


# if __name__ == "__main__":
#     in_f = open("SW Expert/1954. 달팽이 숫자/input.txt", "r")
#     lines = in_f.readlines()
#     T = int(lines[0].strip())

#     for t in range(T):
#         input_ = int(lines[t + 1].strip())
#         print(f"#{t+1}")
#         solve(input_)

# in_f.close()

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        print(f"#{t+1}")
        solve()
