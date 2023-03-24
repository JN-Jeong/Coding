import sys


def solution():
    N, K, Q, M = map(int, sys.stdin.readline().split())
    K_nums = list(map(int, sys.stdin.readline().split()))  # 졸고 있는 학생
    Q_nums = list(map(int, sys.stdin.readline().split()))  # 출석 코드 보낼 학생

    sleeps = [0 for _ in range(N + 3)]
    codes = [0 for _ in range(N + 3)]

    for i in K_nums:
        sleeps[i] = 1

    for i in Q_nums:
        if sleeps[i]:
            continue

        for j in range(i, N + 3, i):
            if not sleeps[j]:
                codes[j] = 1

    cumsum = [0]
    for i in range(1, N + 3):
        cumsum.append(cumsum[-1] + codes[i])

    # print(sleeps)
    # print(codes)
    # print(cumsum)

    for _ in range(M):
        S, E = map(int, sys.stdin.readline().split())
        print(E - S + 1 - (cumsum[E] - cumsum[S - 1]))


if __name__ == "__main__":
    solution()
