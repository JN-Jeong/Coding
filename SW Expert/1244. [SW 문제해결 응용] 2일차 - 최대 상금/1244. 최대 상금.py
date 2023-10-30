"""
SW Expert Academy : 1244. 최대 상금
"""


def solve():
    nums, max_cnt = map(int, (input().split()))
    global answer
    answer = 0

    nums = list(str(nums))
    # print("@", nums)

    visited = {}

    def recur(cnt, n):
        global answer
        if not cnt:
            answer = max(answer, int("".join(n)))
            return

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                n[i], n[j] = n[j], n[i]

                temp = int("".join(n))
                if visited.get((temp, cnt - 1), 1):
                    visited[(temp, cnt - 1)] = 0
                    recur(cnt - 1, n)

                n[i], n[j] = n[j], n[i]

    recur(max_cnt, nums)

    return answer


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        print(f"#{t+1} {solve()}")
