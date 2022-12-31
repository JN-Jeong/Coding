# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    N = int(input())
    dp = [[0, 0] for _ in range(N + 1)]
    dp[1] = [0, 1]

    for i in range(2, N + 1):
        dp[i][0] = (2 * (i - 1) * dp[i - 1][0] + dp[i - 1][1]) % 100000007
        dp[i][1] = ((2 * (i - 1) + 1) * dp[i - 1][0] + dp[i - 1][1]) % 100000007

    return dp[-1][0]


if __name__ == "__main__":
    print(solution())
