from collections import deque
from itertools import combinations


def solution():
    global answer, wall_cnt
    answer = float("inf")
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def spread(viruses, wall_cnt):
        q = deque()
        visited = [[-1] * N for _ in range(N)]
        result = 0

        for virus in viruses:
            y, x = virus
            q.append([y, x])
            visited[y][x] = 0

        while q:
            y, x = q.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] == 0 and visited[ny][nx] == -1:
                        q.append([ny, nx])
                        visited[ny][nx] = visited[y][x] + 1
                        result = max(result, visited[ny][nx])

                    if board[ny][nx] == 2 and visited[ny][nx] == -1:
                        q.append([ny, nx])
                        visited[ny][nx] = visited[y][x] + 1

        cnt = 0
        for y in range(N):
            for x in range(N):
                if visited[y][x] == -1:
                    cnt += 1

        print("@", wall_cnt, cnt)
        for v in visited:
            print(v)
        print()

        if cnt != wall_cnt:
            return float("inf")

        return result

    wall_cnt = 0
    viruses = []
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                wall_cnt += 1

            if board[y][x] == 2:
                viruses.append([y, x])

    for virus in combinations(viruses, M):
        answer = min(answer, spread(virus, wall_cnt))

    if answer == float("inf"):
        return -1
    return answer


if __name__ == "__main__":
    print(solution())
