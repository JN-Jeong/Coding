def solution():
    n, L = map(int, input().split())
    x_locs = list(map(int, input().split()))

    total = 0
    num = 0
    for i in range(n - 1, 0, -1):
        total += x_locs[i]
        num += 1
        if x_locs[i - 1] - L < total / num < x_locs[i - 1] + L:
            continue
        else:
            print("unstable")
            return
    print("stable")


if __name__ == "__main__":
    solution()
