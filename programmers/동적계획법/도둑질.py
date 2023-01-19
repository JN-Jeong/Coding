def solution(money):
    answer = 0

    # 첫 번째 집을 터는 경우
    dp1 = [0 for _ in range(len(money))]
    dp1[0] = money[0]
    dp1[1] = money[0]
    print(dp1)

    for i in range(2, len(dp1) - 1):  # 첫 번째 집을 털면 마지막 집은 털지 못함
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])
    print(dp1)

    # 첫 번째 집을 털지 않는 경우
    dp2 = [0 for _ in range(len(money))]
    dp2[1] = money[1]
    print(dp2)

    for i in range(2, len(dp2)):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])
    print(dp2)

    return max(max(dp1), max(dp2))


moneys = [[1, 2, 3, 1], [1, 1, 1, 99, 1, 1, 99, 1]]
returns = [4, 199]

for money in moneys:
    print(solution(money))
