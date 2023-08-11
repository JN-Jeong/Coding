"""
15. 3Sum
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        N = len(nums)
        answer = []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            s, e = i + 1, N - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    answer.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s - 1]:
                        s += 1

                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0]]
    output = [[[-1, -1, 2], [-1, 0, 1]], [], [[0, 0, 0]]]

    for n in nums:
        print("#", solution.threeSum(n))
