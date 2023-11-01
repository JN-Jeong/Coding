"""
15989. 1,2,3 더하기 4
"""


def solution():
    n = int(input())

    # temp = []

    # def recur(num, nums):
    #     if num == n:
    #         nums.sort()
    #         if nums not in temp:
    #             temp.append(nums)
    #     elif num > n:
    #         return

    #     recur(num + 1, nums + [1])
    #     recur(num + 2, nums + [2])
    #     recur(num + 3, nums + [3])

    # recur(0, [0])

    dp = [1] * 10001
    for i in range(2, 10001):
        dp[i] += dp[i - 2]

    for i in range(3, 10001):
        dp[i] += dp[i - 3]
        
    print(dp[n])

    return


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solution()
