"""
39. Combination Sum
"""

import copy
from collections import deque
from typing import List

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         answer = []

#         def recur(nums, result):
#             total = sum(result)
#             # print("@", result)
#             if total > target:
#                 return

#             if total == target:
#                 answer.append(result)
#                 return

#             for i in range(len(nums)):
#                 recur(nums[i:], result + [nums[i]])
#                 # result.append(nums[i])
#                 # recur(nums[i:], result)

#         recur(candidates, [])

#         return answer


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def recur(idx, result):
            total = sum(result)
            if total > target:
                return

            if total == target:
                # print("@", total, result)
                answer.append(result)
                return

            for i in range(idx, len(candidates)):
                recur(i, result + [candidates[i]])

        recur(0, [])

        return answer


if __name__ == "__main__":
    solution = Solution()
    candidates = [[2, 3, 6, 7], [2, 3, 5], [2], [3, 5, 8], [1, 2]]
    targets = [7, 8, 1, 11, 15]
    output = [[[2, 2, 3], [7]], [[2, 2, 2, 2], [2, 3, 3], [3, 5]], []]

    for i, data in enumerate(zip(candidates, targets)):
        c, t = data
        print(f"#{i}", solution.combinationSum(c, t))
