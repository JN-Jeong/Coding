# 첫 시도
# 실패 (시간 초과 + 오답)
# def solution(people, limit):
#     answer = 0

#     people = sorted(people)
#     print(people)

#     while people:
#         weight = people.pop(0)
#         max_ = weight
#         for i, p in enumerate(people):
#             if weight + p <= limit and weight + p > max_:
#                 max_ = weight + p
#                 answer += 1
#                 people.pop(i)
#                 break
#         else:
#             answer += 1

#     return answer


from collections import deque


def solution(people, limit):
    answer = 0

    people = sorted(people)
    # print(people)

    # 2명을 실을 수 있는 무게가 아닌 사람들은 구명보트 1개씩 먼저 할당
    min_ = min(people)  # or 40
    for i in range(len(people)):
        if min_ + people[i] > limit:
            answer += len(people) - i
            people = people[:i]
            break

    # print(answer)

    q = deque(people)  # 정렬된 리스트를 deque로 만들어줌
    while q:  # deque에서 가장 작은 무게와 큰 무게를 더 했을 때 limit보다 작거나 같으면 2명에 1보트 할당, 크면 1명에 1보트 할당
        if len(q) > 1:
            if q[0] + q[-1] <= limit:
                q.popleft()
                q.pop()
                answer += 1
            else:
                q.pop()
                answer += 1
        else:
            q.pop()
            answer += 1

    return answer


if __name__ == "__main__":
    # people = [70, 60, 60, 50, 70, 65, 80, 90, 30, 40, 90, 35, 80, 70]
    people = [70, 50, 80, 50]
    limit = 100
    print(solution(people, limit))
