from collections import deque


def solution():
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(board)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    answer = 0
    while True:
        temp_board = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if 0 <= x + 1 < N and L <= abs(board[y][x] - board[y][x + 1]) <= R:
                    temp_board[y][x] = 1
                    temp_board[y][x + 1] = 1
                if 0 <= y + 1 < N and L <= abs(board[y][x] - board[y + 1][x]) <= R:
                    temp_board[y][x] = 1
                    temp_board[y + 1][x] = 1

        visited = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                q = deque()
                q.append([y, x])
                locs = set((y, x))

                while q:
                    y, x = q.popleft()

                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            q.append([ny, nx])
                            locs.add((ny, nx))

                num = 0
                for loc in locs:
                    y, x = loc
                    board[y][x] = num // len(locs)

        if locs:
            answer += 1
            num = 0
            for loc in locs:
                y, x = loc
                num += board[y][x]

            for loc in locs:
                y, x = loc
                board[y][x] = num // len(locs)

            for b in board:
                print(b)
            print()

            continue

        break

    # for b in board:
    #     print(b)
    # print()
    print(answer)


if __name__ == "__main__":
    solution()
