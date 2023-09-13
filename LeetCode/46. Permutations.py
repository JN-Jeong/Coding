"""
46. Permutations
"""

from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def recur(permu, visited):
            if len(permu) == len(nums):
                answer.append(permu)
                return

            for i in range(len(nums)):
                if visited[i] == 0:
                    visited[i] = 1
                    recur(permu + [nums[i]], visited)
                    visited[i] = 0

        visited = [0] * len(nums)
        for i in range(len(nums)):
            visited[i] = 1
            recur([nums[i]], visited)
            visited[i] = 0

        # answer = list(map(list, permutations(nums, len(nums))))
        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[1, 2, 3], [0, 1], [1]]
    output = [[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], [[0, 1], [1, 0]], [[1]]]

    for n in nums:
        print("#", solution.permute(n))
