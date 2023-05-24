def solution():
    N, K = map(int, input().split())
    eratos = [1 for _ in range(N + 1)]

    def solve():
        cnt = 0
        for i in range(2, N + 1):
            if eratos[i] == 1:
                for j in range(i, N + 1, i):
                    if eratos[j] == 0:
                        continue
                    eratos[j] = 0
                    # print(j)
                    cnt += 1
                    if cnt == K:
                        return j

    print(solve())


if __name__ == "__main__":
    solution()
