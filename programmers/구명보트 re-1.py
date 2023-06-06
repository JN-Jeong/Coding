"""
굳이 pop 해주지 않고 index 포인터로 옮겨가면서 계산해줘도 됨
"""

from collections import deque


def solution(people, limit):
    answer = 0

    people.sort()
    q = deque(people)

    while q:
        if len(q) > 1:
            if q[0] + q[-1] <= limit:
                answer += 1
                q.popleft()
                q.pop()
            else:
                answer += 1
                q.pop()
        else:
            answer += 1
            q.pop()

    return answer


if __name__ == "__main__":
    peoples = [[70, 60, 60, 50, 70, 65, 80, 90, 30, 40, 90, 35, 80, 70], [70, 50, 80, 50], [70, 80, 50]]
    limits = [100, 100, 100]

    for people, limit in zip(peoples, limits):
        print(solution(people, limit))
