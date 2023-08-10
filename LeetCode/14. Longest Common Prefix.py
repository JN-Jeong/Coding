"""
14. Longest Common Prefix
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float("inf")
        for s in strs:
            length = min(length, len(s))

        answer = ""
        for i in range(length):
            temp = strs[0][: i + 1]
            for j in range(1, len(strs)):
                if temp != strs[j][: i + 1]:
                    return answer
            answer = temp

        return answer


if __name__ == "__main__":
    solution = Solution()
    strs = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
    output = ["fl", ""]

    for s in strs:
        print("#", solution.longestCommonPrefix(s))
