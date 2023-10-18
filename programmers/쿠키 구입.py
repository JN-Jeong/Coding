"""
프로그래머스 : 쿠키 구입
"""


def solution(cookie):
    if len(cookie) == 1:
        return 0
    answer = 0

    sum_arr = [0]
    for i in range(len(cookie)):
        sum_arr.append(sum_arr[-1] + cookie[i])

    print(sum_arr)

    for mid in range(1, len(cookie)):
        start = 0
        end = len(cookie)

        while start < mid and end >= mid:
            son1 = sum_arr[mid] - sum_arr[start]
            son2 = sum_arr[end] - sum_arr[mid]

            if son1 == son2:
                answer = max(answer, son1)
                break

            if son1 > son2:
                start += 1
            else:
                end -= 1

    return answer


if __name__ == "__main__":
    cookie = [[1, 1, 2, 3], [1, 2, 4, 5]]
    results = [3, 0]

    for i, data in enumerate(cookie):
        c = data
        print(f"#{i}", solution(c))
