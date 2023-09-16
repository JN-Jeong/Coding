"""
프로그래머스 : 거스름돈
"""


def solution(n, money):
    dp = [1] + [0] * n

    for coin in money:
        for price in range(coin, n + 1):
            dp[price] += dp[price - coin]

    print(dp)
    return dp[n] % 10000000007


if __name__ == "__main__":
    nums = [5]
    money = [[1, 2, 5]]
    result = [4]

    for i, data in enumerate(zip(nums, money)):
        n, m = data
        print(f"#{i}", solution(n, m))
