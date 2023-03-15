def solution():
    N, K = map(int, input().split())
    array = list(map(int, input().split()))

    nums = [0] * (max(array) + 1)
    lp, rp = 0, 0
    answer = 0
    while rp < N:
        if nums[array[rp]] < K:
            nums[array[rp]] += 1
            rp += 1
        else:
            nums[array[lp]] -= 1
            lp += 1
        answer = max(answer, rp - lp)
        # print(lp, rp, nums)

    print(answer)


if __name__ == "__main__":
    solution()
