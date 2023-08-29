"""
22. Generate Parentheses
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def recur(left, right, string):
            if len(string) == n * 2:
                answer.append(string)
                return

            if left < n:
                recur(left + 1, right, string + "(")

            if right < left:
                recur(left, right + 1, string + ")")

        recur(0, 0, "")
        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 1]
    output = [["((()))", "(()())", "(())()", "()(())", "()()()"], ["()"]]

    for n in nums:
        print("#", solution.generateParenthesis(n))
