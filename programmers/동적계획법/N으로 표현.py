"""
1. N 추가
2. N 더하기
3. N 빼기
4. N 곱하기
5. N 나누기
"""


def solution(N, number):
    answer = 0

    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for first in dp[j]:
                for second in dp[i - j]:  # 숫자를 n번 사용했을 때 가능한 연산 : i + j = n
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(first * second)
                    if second != 0:
                        dp[i].add(first // second)
                    # if first != 0:
                    #     dp[i].add(second // first)

        print(i, dp)
        if number in dp[i]:
            return i

    return -1


Ns = [5, 2]
numbers = [12, 11]
returns = [4, 3]

for n, num in zip(Ns, numbers):
    print(solution(n, num))
