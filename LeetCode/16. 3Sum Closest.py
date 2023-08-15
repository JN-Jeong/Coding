"""
16. 3Sum Closest
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = nums[0] + nums[1] + nums[2]

        N = len(nums)
        for i in range(N - 2):
            s, e = i + 1, N - 1
            while s < e:
                total = nums[i] + nums[s] + nums[e]
                if total == target:
                    return total

                if abs(total - target) < abs(answer - target):
                    answer = total

                if total < target:
                    s += 1
                elif total > target:
                    e -= 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[-1, 2, 1, -4], [0, 0, 0]]
    target = [1, 1]
    output = [2, 0]

    for n, t in zip(nums, target):
        print("#", solution.threeSumClosest(n, t))
