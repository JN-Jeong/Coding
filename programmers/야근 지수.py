"""
프로그래머스 : 야근 지수
"""

import heapq


def solution(n, works):
    if n >= sum(works):
        return 0
    answer = 0

    works = [-w for w in works]
    heapq.heapify(works)
    # print("@", works)

    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
        # print("@@", works)

    for w in works:
        answer += w**2

    return answer


if __name__ == "__main__":
    works = [[4, 3, 3], [2, 1, 2], [1, 1]]
    n = [4, 1, 3]
    results = [12, 6, 0]

    for i, data in enumerate(zip(works, n)):
        w, n = data
        print(f"#{i}", solution(n, w))
