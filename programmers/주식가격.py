"""
각 주식의 가격이 떨어지지 않은 기간이 몇 초인지 list로 반환
"""

from collections import deque


def solution(prices):
    answer = []

    q = deque(prices)

    while q:
        price = q.popleft()
        time = 0

        for i in q:
            time += 1
            if price > i:
                break
        answer.append(time)

    return answer


prices = [
    [1, 2, 3, 2, 3],
]
result = [
    [4, 3, 1, 1, 0],
]

for price in prices:
    print(solution(price))
