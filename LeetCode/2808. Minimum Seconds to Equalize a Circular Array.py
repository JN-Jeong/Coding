"""
2808. Minimum Seconds to Equalize a Circular Array
"""

from collections import defaultdict
from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        nums += nums
        pos, gap = {}, defaultdict(lambda: 0)
        for i, n in enumerate(nums):
            if n in pos:
                gap[n] = max(gap[n], (i - pos[n]) // 2)
            pos[n] = i
            print("@", i)
            print("@@", pos, gap.items())

        return min(gap.values())


if __name__ == "__main__":
    solution = Solution()
    nums = [[1, 2, 1, 2], [2, 1, 3, 3, 2], [5, 5, 5, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    output = [1, 2, 0]

    for i, n in enumerate(nums):
        print(f"#{i}", solution.minimumSeconds(n))
