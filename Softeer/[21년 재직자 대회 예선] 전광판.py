"""
https://softeer.ai/practice/6268
[21년 재직자 대회 예선] 전광판
"""

import sys


def solution():
    T = int(input())

    nums = {
        "n": 0b0000000,
        "0": 0b1110111,
        "1": 0b0010010,
        "2": 0b1011101,
        "3": 0b1011011,
        "4": 0b0111010,
        "5": 0b1101011,
        "6": 0b1101111,
        "7": 0b1110010,
        "8": 0b1111111,
        "9": 0b1111011,
    }
    # print("@", nums)
    # print("@@", bin(0b1111 & 0b0111))
    # print("@@@", bin(nums["1"] ^ nums["2"]))
    # print("@@@@", str(bin(nums["0"] ^ nums["9"])).count("1"))

    for _ in range(T):
        num_a, num_b = input().split()
        num_a = num_a.rjust(5, "n")
        num_b = num_b.rjust(5, "n")
        # print("@", num_a, num_b)

        result = 0
        for a, b in zip(num_a, num_b):
            temp = str(bin(nums[a] ^ nums[b])).count("1")
            # print("@@", temp)
            result += temp
        print(result)


if __name__ == "__main__":
    solution()
