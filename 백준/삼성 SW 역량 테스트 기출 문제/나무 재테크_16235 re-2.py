from collections import deque


def solution():
    N, M, K = map(int, input().split())
    board = [[5] * N for _ in range(N)]
    S2D2 = [list(map(int, input().split())) for _ in range(N)]
    trees = [[deque() for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        y, x, z = map(int, input().split())
        trees[y - 1][x - 1].append(z)

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    for _ in range(K):
        # 봄, 여름
        for y in range(N):
            for x in range(N):
                if trees[y][x]:
                    for z in range(len(trees[y][x])):
                        age = trees[y][x][z]
                        if board[y][x] >= age:
                            trees[y][x][z] += 1
                            board[y][x] -= age
                        else:
                            for _ in range(z, len(trees[y][x])):
                                board[y][x] += trees[y][x].pop() // 2
                            break

        # 가을
        for y in range(N):
            for x in range(N):
                if trees[y][x]:
                    for z in range(len(trees[y][x])):
                        if trees[y][x][z] % 5 == 0:
                            for d in range(8):
                                ny = y + dy[d]
                                nx = x + dx[d]
                                if 0 <= ny < N and 0 <= nx < N:
                                    trees[ny][nx].appendleft(1)

        # 겨울
        for y in range(N):
            for x in range(N):
                board[y][x] += S2D2[y][x]

    # for t in trees:
    #     print(t)

    answer = 0
    for y in range(N):
        for x in range(N):
            answer += len(trees[y][x])

    return answer


if __name__ == "__main__":
    print(solution())
