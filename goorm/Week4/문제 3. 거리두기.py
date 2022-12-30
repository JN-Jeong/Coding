# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    N = int(input())
    dp = [[1] * 5 for _ in range(N + 1)]
    for i in range(2, N + 1):
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]) % 100000007
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % 100000007
        dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % 100000007
        dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 100000007
        dp[i][4] = (dp[i - 1][0] + dp[i - 1][2]) % 100000007

    return (sum(dp[-1])) % 100000007


if __name__ == "__main__":
    print(solution())
