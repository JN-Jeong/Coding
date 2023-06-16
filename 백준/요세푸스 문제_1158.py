def solution():
    answer = []
    N, K = map(int, input().split())
    arr = [i for i in range(1, N + 1)]

    idx = 0
    for i in range(N):
        idx += K - 1
        if idx >= len(arr):
            idx = idx % len(arr)
        print(idx + 1)

        answer.append(str(arr.pop(idx)))

    print("<", ", ".join(answer)[:], ">", sep="")


if __name__ == "__main__":
    solution()
