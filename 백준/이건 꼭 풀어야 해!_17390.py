import sys


def solution():
    N, Q = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()

    cumsum = [0]
    for i in range(len(A)):
        cumsum.append(cumsum[-1] + A[i])

    for i in range(Q):
        L, R = map(int, sys.stdin.readline().split())
        print(cumsum[R] - cumsum[L - 1])


if __name__ == "__main__":
    solution()
