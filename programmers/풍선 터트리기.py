"""
프로그래머스 : 풍선 터트리기
"""


def solution(a):
    answer = 0

    left_mins = [a[0]]
    right_mins = [a[-1]]
    for i in range(1, len(a)):
        # left
        if left_mins[-1] > a[i]:
            left_mins.append(a[i])
        else:
            left_mins.append(left_mins[-1])

        # right
        if right_mins[-1] > a[len(a) - 1 - i]:
            right_mins.append(a[len(a) - 1 - i])
        else:
            right_mins.append(right_mins[-1])
    right_mins = right_mins[::-1]

    print(left_mins)
    print(right_mins)

    for i in range(1, len(a) - 1):
        if left_mins[i - 1] > a[i] or right_mins[i + 1] > a[i]:
            answer += 1

    return answer + 2


if __name__ == "__main__":
    arr = [[9, -1, -5], [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]]
    results = [3, 6]

    for i, data in enumerate(arr):
        a = data
        print(f"#{i}", solution(a))
