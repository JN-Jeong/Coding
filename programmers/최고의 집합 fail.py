"""
프로그래머스 : 최고의 집합
"""


def solution(n, s):
    global answer, max_multi
    answer = []
    max_multi = 0

    def recur(n, cnt, nums, total):
        global answer, max_multi
        if total > s:
            return

        if cnt == n and total == s:
            total_multi = 1
            for num in nums:
                total_multi = total_multi * num

            if max_multi < total_multi:
                answer = nums
                max_multi = total_multi

            return

        for i in range(1, s + 1):
            recur(n, cnt + 1, nums + [i], total + i)

    recur(n, 0, [], 0)

    if answer:
        return answer
    return [-1]


if __name__ == "__main__":
    list_n = [2, 2, 2, 2, 3, 5000]
    list_s = [9, 1, 8, 13, 13, 25394]
    result = [[4, 5], [-1], [4, 4]]

    for i, data in enumerate(zip(list_n, list_s)):
        n, s = data
        print(f"#{i}", solution(n, s))
