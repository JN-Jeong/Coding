"""
3. Longest Substring Without Repeating Characters
"""

from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""

        def search(s, l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        for i in range(len(s)):
            temp_even = search(s, i, i + 1)
            if len(temp_even) > len(answer):
                answer = temp_even

            temp_odd = search(s, i, i)
            if len(temp_odd) > len(answer):
                answer = temp_odd

        return answer


if __name__ == "__main__":
    solution = Solution()
    s = ["babad", "cbbd"]
    output = ["bab", "bb"]

    for c in s:
        print("#", solution.longestPalindrome(c))
