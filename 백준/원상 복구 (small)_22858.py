def solution():
    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    D = list(map(int, input().split()))

    for _ in range(K):
        P = [0] * N
        for i, idx in enumerate(D):
            P[idx - 1] = S[i]
            # print(i, P)
        S = P

    print(*P)


if __name__ == "__main__":
    solution()
