"""
27. Remove Element
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                answer -= 1

        for i in range(len(nums)):
            if nums[i] == "_":
                idx = i + 1
                while idx < len(nums):
                    if nums[idx] != "_":
                        nums[i], nums[idx] = nums[idx], nums[i]

                    idx += 1

        return (answer, nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [[3, 2, 2, 3], [0, 1, 2, 2, 3, 0, 4, 2]]
    vals = [3, 2]
    output = [[2, [2, 2, "_", "_"]], [5, [0, 1, 4, 0, 3, "_", "_", "_"]]]

    for n, v in zip(nums, vals):
        print("#", solution.removeElement(n, v))
