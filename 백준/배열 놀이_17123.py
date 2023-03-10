def solution():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(N)]
        total_rows = [0] * N
        total_cols = [0] * N
        for i in range(N):
            total_rows[i] = sum(A[i])

        for j in range(N):
            for i in range(N):
                total_cols[j] += A[i][j]

        for _ in range(M):
            r1, c1, r2, c2, v = map(int, input().split())
            num = (r2 - (r1 - 1)) * (c2 - (c1 - 1))
            total = v * num
            each_row = total // (r2 - (r1 - 1))
            each_col = total // (c2 - (c1 - 1))
            for r in range(r1 - 1, r2):
                total_rows[r] += each_row
            for c in range(c1 - 1, c2):
                total_cols[c] += each_col

        for n in total_rows:
            print(n, end=" ")
        print()
        for n in total_cols:
            print(n, end=" ")
        print()


if __name__ == "__main__":
    solution()
