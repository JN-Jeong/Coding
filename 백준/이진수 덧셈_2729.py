def solution():
    T = int(input())
    for _ in range(T):
        a, b = input().split()
        temp_a = 0
        temp_b = 0
        for i, n in enumerate(a[::-1]):
            temp_a += int(n) * (2**i)
        for i, n in enumerate(b[::-1]):
            temp_b += int(n) * (2**i)

        print(int(bin(temp_a + temp_b)[2:]))


if __name__ == "__main__":
    solution()
