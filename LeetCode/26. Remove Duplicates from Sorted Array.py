"""
26. Remove Duplicates from Sorted Array
"""

from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         answer = len(nums)
#         for i in range(len(nums) - 1):
#             if nums[i] != "_" and nums[i] == nums[i + 1]:
#                 idx = i + 1
#                 while idx < len(nums):
#                     if nums[idx] == nums[i]:
#                         nums[idx] = "_"
#                         answer -= 1
#                     idx += 1

#         for i in range(1, len(nums)):
#             if nums[i] != "_":
#                 idx = i - 1
#                 while idx >= 0:
#                     if nums[idx] != "_" and nums[idx + 1] == "_":
#                         nums[i], nums[idx + 1] = nums[idx + 1], nums[i]
#                         break
#                     idx -= 1

#         print(nums)
#         return answer


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                answer += 1
            else:
                nums[i - answer] = nums[i]

        print(nums)
        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    output = [[2, [1, 2, "_"]], [5, [0, 1, 2, 3, 4, "_", "_", "_", "_", "_"]]]

    for n in nums:
        print("#", solution.removeDuplicates(n))
