import math


def solution():
    N = input()
    nums = [0 for _ in range(10)]

    for num in N:
        if num == "6" or num == "9":
            nums[6] += 0.5
        else:
            nums[int(num)] += 1

    # print(nums)
    print(math.ceil(max(nums)))


if __name__ == "__main__":
    solution()
