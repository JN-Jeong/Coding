"""
- 서쪽에 1개이면 동쪽에 지을 수 있는 개수가 경우의 수가 됨
- 서쪽과 동쪽이 지을 수 있는 개수가 같으면 경우의 수는 1이 됨
- 서쪽보다 동쪽에 지을 수 있는 개수가 많으면 
   (서쪽 N, 동쪽 M-1개로 다리를 지을 수 있는 경우의 수) + (서쪽 N-1, 동쪽 M-1개로 다리를 지을 수 있는 경우의 수)가 경우의 수가 됨
   Dynamic Programming

or 

조합 사용
mCn = m! / (n! * (m-n)!)
"""

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1:
                dp[i][j] = j
            elif i == j:
                dp[i][j] = 1
            elif j > i:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    print(dp)
    print(dp[N][M])
