from collections import deque


def melt(ice):
    N = len(ice)
    melted = []
    for i in range(N):
        for j in range(N):
            if ice[i][j]:
                count = 0
                for a, b in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= a < N and 0 <= b < N:
                        if ice[a][b]:
                            count += 1
                if count < 3:
                    melted.append([i, j])

    for x, y in melted:
        ice[x][y] -= 1


def rot(ice, L, N):
    if L:
        for i in range(2 ** (N - L)):
            for j in range(2 ** (N - L)):
                tmp = []
                for k in range(2**L):
                    tmp.append(ice[i * (2**L) + k][j * (2**L) : (j + 1) * (2**L)])
                for a in range(2**L):
                    for b in range(2**L):
                        ice[i * (2**L) + a][j * (2**L) + b] = tmp[2**L - 1 - b][a]


def bfs(ice, x, y):
    mass = 0
    if ice[x][y] == 0:
        return mass

    N = len(ice)
    q = deque([[x, y]])
    ice[x][y] = 0
    while q:
        x, y = q.popleft()
        mass += 1
        for a, b in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            if 0 <= a < N and 0 <= b < N:
                if ice[a][b]:
                    q.append([a, b])
                    ice[a][b] = 0

    return mass


def solution():
    N, Q = map(int, input().split())

    ice = []
    for _ in range(2**N):
        ice.append(list(map(int, input().split())))

    L_list = list(map(int, input().split()))

    for L in L_list:
        rot(ice, L, N)
        melt(ice)

    total = 0
    for i in range(2**N):
        total += sum(ice[i])

    mass = 0
    for i in range(2**N):
        for j in range(2**N):
            mass = max(bfs(ice, i, j), mass)

    return total, mass


if __name__ == "__main__":
    total, mass = solution()

    print(total)
    print(mass)
