"""
전적이 n-1인 선수는 순위를 매길 수 있음
i번 선수를 이긴 선수는 i한테 진 선수들한테도 이김
i번 선수한테 진 선수는 i한테 이긴 선수들한테도 짐
"""


def solution(n, results):
    answer = 0

    winners = dict()
    losers = dict()
    for winner, loser in results:
        winners.setdefault(loser, set())
        winners[loser].add(winner)
        losers.setdefault(winner, set())
        losers[winner].add(loser)
    print(f"winners : {winners}, losers : {losers}")

    for i in range(1, n + 1):
        winners.setdefault(i, set())
        losers.setdefault(i, set())
        for winner in winners[i]:
            losers[winner].update(losers[i])
        for loser in losers[i]:
            winners[loser].update(winners[i])
    print(f"winners : {winners}, losers : {losers}")

    for i in range(1, n + 1):
        if len(winners[i]) + len(losers[i]) == n - 1:  # i의 전적이 n-1번이면 순위를 매길 수 있음
            answer += 1

    return answer


n = [5, 5]  # 선수의 수
results = [[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]], [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [1, 3], [1, 4]]]  # 경기 결과
returns = [
    2,
]

for num, result in zip(n, results):
    print(solution(num, result))
