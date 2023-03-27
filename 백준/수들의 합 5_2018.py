def solution():
    N = int(input())
    lp, rp = 1, 1
    temp = 1
    answer = 1

    while rp < N:
        if temp == N:
            # print("#", lp, rp)
            answer += 1
            rp += 1
            temp += rp
        elif temp > N:
            temp -= lp
            lp += 1
        elif temp < N:
            rp += 1
            temp += rp
        # print(lp, rp)

    print(answer)


if __name__ == "__main__":
    solution()
