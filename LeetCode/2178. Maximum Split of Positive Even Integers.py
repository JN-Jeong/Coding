"""
2178. Maximum Split of Positive Even Integers
"""
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        answer = set()
        if finalSum % 2 != 0:
            return answer

        total = 0
        i = 2
        while total < finalSum:
            total += i
            answer.add(i)
            i += 2

        if total == finalSum:
            return answer
        else:
            answer.discard(total - finalSum)
            return answer


if __name__ == "__main__":
    solution = Solution()
    finalSum = [12, 7, 28]
    output = [[2, 4, 6], [], [6, 8, 2, 12]]

    for s in finalSum:
        print("#", solution.maximumEvenSplit(s))
