"""
239. Sliding Window Maximum
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        q = deque()

        for i in range(len(nums)):
            if q and q[0] == i - k:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                print("@", q, nums[i], i)
                q.pop()
                print("!@", q, nums[i], i)

            q.append(i)
            if i >= k - 1:
                answer.append(nums[q[0]])

            print("@@", q)
            print("@@@", i, answer)

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[1, 3, -1, -3, 5, 3, 6, 7], [1], [1, 2, 3]]
    ks = [3, 1, 3]
    output = [[3, 3, 5, 5, 6, 7], [1], [3]]

    for n, k in zip(nums, ks):
        print("#", solution.maxSlidingWindow(n, k))
