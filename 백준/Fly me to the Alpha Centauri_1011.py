def solution():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        diff = y - x
        n = int(diff**0.5)
        z = diff - n**2

        if diff == 0:
            print(0)
        else:
            if diff == n**2:
                print(2 * n - 1)
            elif z <= n:
                print(2 * n)
            else:
                print(2 * n + 1)


if __name__ == "__main__":
    solution()
