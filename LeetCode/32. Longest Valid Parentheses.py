"""
32. Longest Valid Parentheses

"""

from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        stacks = [-1]
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stacks.append(i)
            elif c == ")":
                stacks.pop()
                if stacks:
                    answer = max(answer, i - stacks[-1])
                else:
                    stacks.append(i)
            print(answer, i, stacks)

        return answer


if __name__ == "__main__":
    solution = Solution()
    strings = ["(()", ")()())", "", "(()()))", "()(()", "()(())", "((()))", ")))()"]
    output = [2, 4, 0, 6, 2, 6, 6, 2]

    for s in strings:
        print("#", solution.longestValidParentheses(s))
