"""
프로그래머스 : 숫자의 표현
"""


def solution(n):
    answer = 0
    arr = [i + 1 for i in range(n)]
    # print(arr)

    start, end = 0, 1
    while end <= n:
        if sum(arr[start:end]) == n:
            # print("@", answer, start, end)
            # print("@@", sum(arr[start:end]))
            answer += 1
            start += 1
        elif sum(arr[start:end]) < n:
            end += 1
        elif sum(arr[start:end]) > n:
            start += 1

    return answer


if __name__ == "__main__":
    ns = [15, 20]
    result = [4]

    for i, data in enumerate(ns):
        n = data
        print(f"#{i}", solution(n))
