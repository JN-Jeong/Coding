"""
18. 4Sum
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        answer = set()
        N = len(nums)
        for i in range(N - 3):
            for j in range(i + 1, N - 2):
                total = nums[i] + nums[j]
                s, e = j + 1, N - 1
                while s < e:
                    result = nums[s] + nums[e]
                    if total + result == target:
                        answer.add((nums[i], nums[j], nums[s], nums[e]))
                        s += 1
                        e -= 1

                    elif total + result < target:
                        s += 1

                    else:
                        e -= 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[1, 0, -1, 0, -2, 2], [2, 2, 2, 2, 2], [0, 0, 0, 0]]
    target = [0, 8, 0]
    output = [[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], [[2, 2, 2, 2]]]

    for n, t in zip(nums, target):
        print("#", solution.fourSum(n, t))
