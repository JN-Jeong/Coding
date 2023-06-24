def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    clouds = [[N - 1, 0], [N - 1, 1], [N - 1 - 1, 0], [N - 1 - 1, 1]]

    #  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    for _ in range(M):
        d, s = map(int, input().split())

        # 구름 이동
        for i, c in enumerate(clouds):
            cy, cx = c
            ncy = (cy + dy[d - 1] * s) % N
            ncx = (cx + dx[d - 1] * s) % N
            clouds[i] = [ncy, ncx]

            # 물의 양 증가
            board[ncy][ncx] += 1

        visited = [[0] * N for _ in range(N)]
        # 물복사버그
        for cy, cx in clouds:
            water = 0
            visited[cy][cx] = 1
            for d in range(1, 8, 2):
                nrow = cy + dy[d]
                ncol = cx + dx[d]
                if 0 <= nrow < N and 0 <= ncol < N and board[nrow][ncol] > 0:
                    water += 1
            board[cy][cx] += water

        # 구름 생성
        clouds = []
        for y in range(N):
            for x in range(N):
                if board[y][x] >= 2 and visited[y][x] == 0:
                    clouds.append([y, x])
                    board[y][x] -= 2

        # 리스트 복사와 탐색((y,x) in clouds)에 걸리는 시간 차이가 큰듯...

    answer = 0
    for y in range(N):
        for x in range(N):
            answer += board[y][x]
    print(answer)


if __name__ == "__main__":
    solution()
