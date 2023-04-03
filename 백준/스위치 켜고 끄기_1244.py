def solution():
    n = int(input())
    switches = list(map(int, input().split()))
    n_student = int(input())
    for _ in range(n_student):
        sex, num = map(int, input().split())

        if sex == 1:  # 남학생
            for i in range(n):
                if (i + 1) % num == 0:
                    switches[i] = (switches[i] + 1) % 2
        elif sex == 2:  # 여학생
            left, right = num - 1, num - 1
            while left >= 0 and right < n:
                if switches[left] != switches[right]:
                    break

                left -= 1
                right += 1

            for i in range(left + 1, right):
                switches[i] = (switches[i] + 1) % 2

    for i, n in enumerate(switches):
        if i != 0 and i % 20 == 0:
            print()
        print(n, end=" ")


if __name__ == "__main__":
    solution()
