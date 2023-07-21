"""
42. Trapping Rain Water
"""


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        max_left, max_right = height[0], height[n - 1]
        left, right = 1, n - 2
        answer = 0

        while left <= right:
            if max_left < max_right:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    answer += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    answer += max_right - height[right]
                right -= 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    height = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [4, 2, 0, 3, 2, 5]]
    output = [6, 9]

    for h in height:
        print(solution.trap(h))
