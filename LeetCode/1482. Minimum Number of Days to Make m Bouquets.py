from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        length = len(bloomDay)
        bloomed = [0] * length

        if m * k > length:
            return -1

        def check():
            total = 0
            idx = 0
            while idx < length:
                flowers = 0
                for i in range(idx, min(length, idx + k)):
                    if bloomed[i]:
                        flowers += 1
                    else:
                        break
                if flowers == k:
                    total += 1
                    idx = i
                idx += 1

            if total == m:
                return True
            return False

        day = 1
        while True:
            for i in range(length):
                if bloomDay[i] == day:
                    bloomed[i] = 1

            if check():
                return day

            day += 1


if __name__ == "__main__":
    solution = Solution()
    bloomDays = [[1, 10, 3, 10, 2], [1, 10, 3, 10, 2], [7, 7, 7, 7, 12, 7, 7], [1000000000, 1000000000]]
    m = [3, 3, 2, 1]
    k = [1, 2, 3, 1]

    for a, b, c in zip(bloomDays, m, k):
        print(solution.minDays(a, b, c))
