def solution():
    N = int(input())
    n = int(input())

    board = [[0] * N for _ in range(N)]

    # 하 우 상 좌
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    dir = 0
    num = N**2
    y, x = 0, 0
    while num > 0:
        if num == n:
            answer = y + 1, x + 1
        board[y][x] = num

        ny = y + dy[dir]
        nx = x + dx[dir]
        while ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 0:
            if num == 1:
                break
            dir = (dir + 1) % 4
            ny = y + dy[dir]
            nx = x + dx[dir]

        y = ny
        x = nx
        num -= 1
        # print(num)

    for b in board:
        print(*b)
    print(*answer)


if __name__ == "__main__":
    solution()
