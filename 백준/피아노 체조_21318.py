import sys


def solution():
    N = int(sys.stdin.readline())
    musics = list(map(int, sys.stdin.readline().split()))
    fails = [0] * N
    for i in range(1, N):
        if musics[i - 1] > musics[i]:
            fails[i - 1] = 1

    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[-1] + fails[i])

    # print(musics)
    # print(fails)
    # print(cumsum)

    Q = int(sys.stdin.readline())
    for _ in range(Q):
        x, y = map(int, sys.stdin.readline().split())
        print(cumsum[y - 1] - cumsum[x - 1])

    pass


if __name__ == "__main__":
    solution()
