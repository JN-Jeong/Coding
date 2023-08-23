"""
41. First Missing Positive
"""

from typing import List, Optional


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        answer = 1
        nums.sort()

        for n in nums:
            if answer == n:
                answer += 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12]]
    output = [3, 2, 1]

    for n in nums:
        print("#", solution.firstMissingPositive(n))
