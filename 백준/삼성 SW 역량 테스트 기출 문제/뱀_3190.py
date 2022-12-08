def solution():
    time = 0
    N = int(input())  # 보드 크기
    K = int(input())  # 사과 개수

    board = [[0] * N for _ in range(N)]
    board[0][0] = 1  # 뱀의 처음 위치

    for _ in range(K):
        x, y = map(int, input().split())
        board[x - 1][y - 1] = 2  # 사과 위치

    L = int(input())  # 방향 변환 정보
    directions = {}
    for _ in range(L):
        t, d = input().split()
        if d == "L":
            directions[int(t)] = 1
        else:
            directions[int(t)] = -1

    dir = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 우 상 좌 하
    x, y = 0, 0
    snake = [(0, 0)]
    dir_idx = 0
    while True:
        time += 1
        nx = x + dir[dir_idx][0]
        ny = y + dir[dir_idx][1]

        if not (0 <= nx < N and 0 <= ny < N):  # 벽에 부딪히면 종료
            break

        if board[nx][ny] == 2:  # 사과가 있다면
            board[nx][ny] = 1
            snake.append((nx, ny))
            x, y = nx, ny
        elif board[nx][ny] == 1:  # 자기 몸과 부딪히면 종료
            break
        else:  # 사과가 없다면
            snake.append((nx, ny))
            board[nx][ny] = 1
            row, col = snake.pop(0)
            board[row][col] = 0
            x, y = nx, ny

        # for b in board:
        #     print(b)
        # print()

        if time in directions:
            dir_idx = (dir_idx + directions[time]) % 4
            # print(dir_idx)

    return time


if __name__ == "__main__":
    print(solution())
