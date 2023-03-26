import sys


def solution():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    cumsum = [0]
    for i in range(1, len(A) + 1):
        cumsum.append(cumsum[-1] + A[i - 1])

    for i in range(M):
        i, j = map(int, sys.stdin.readline().split())
        print(cumsum[j] - cumsum[i - 1])


if __name__ == "__main__":
    solution()
