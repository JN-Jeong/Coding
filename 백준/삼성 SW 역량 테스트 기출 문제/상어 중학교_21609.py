from collections import deque


def solution():
    answer = 0
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    while True:
        visited = [[0] * N for _ in range(N)]
        blocks = []
        for i in range(N):
            for j in range(N):
                if board[i][j] > 0 and visited[i][j] == 0:
                    visited[i][j] = 1
                    block_info = bfs(i, j, board, visited, N)
                    # block_info = [블록 개수, 무지개블록 개수, 블록 좌표]
                    if block_info[0] >= 2:
                        blocks.append(block_info)
        blocks.sort(reverse=True)
        print(blocks)

        if not blocks:
            break

        remove(blocks[0][2], board)
        answer += blocks[0][0] ** 2

        gravity(board, N)
        board = rot90(board, N)
        gravity(board, N)

    return answer


def bfs(x, y, board, visited, N):
    color = board[x][y]
    q = deque()
    q.append([x, y])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt, rainbow_cnt = 1, 0  # 블록개수, 무지개블록 개수
    blocks, rainbows = [[x, y]], []  # 블록좌표 넣을 리스트, 무지개좌표 넣을 리스트

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 안이면서 방문 안한 일반 블록인 경우
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] == color:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])

            # 범위 안이면서 방문 안한 무지개 블록인 경우
            elif 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # 무지개블록은 방문 다시 해제
    for x, y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks + rainbows]


def remove(block, board):
    for x, y in block:
        board[x][y] = -2
    # for b in board:
    #     print(b)
    # print()


def gravity(board, N):
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if board[i][j] > -1:
                row = i
                while True:
                    if 0 <= row + 1 < N and board[row + 1][j] == -2:
                        board[row + 1][j], board[row][j] = board[row][j], board[row + 1][j]
                        row += 1
                    else:
                        break


def rot90(board, N):
    # temp = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         temp[N - 1 - j][i] = board[i][j]

    # return temp
    temp = list(map(int, zip(*board)))[::-1]
    return temp


if __name__ == "__main__":
    print(solution())
