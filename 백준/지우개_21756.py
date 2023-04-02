def solution():
    N = int(input())

    i = 0
    num = 2
    while num <= N:
        i += 1
        num = num * 2
    print(num // 2)


if __name__ == "__main__":
    solution()
