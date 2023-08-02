"""
3. Longest Substring Without Repeating Characters
"""

from typing import List

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         answer = 0
#         for i in range(len(s)):
#             cnt = 0
#             temp = []

#             for j in range(i, len(s)):
#                 if s[j] in temp:
#                     break
#                 cnt += 1
#                 temp.append(s[j])

#             answer = max(answer, cnt)
#         return answer


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                """
                If s[r] not in seen, we can keep increasing the window size by moving right pointer
                """
                output = max(output, r - l + 1)
            else:
                """
                There are two cases if s[r] in seen:
                case1: s[r] is not inside the current window, we can keep increase the window
                case2: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
                """
                if seen[s[r]] < l:
                    output = max(output, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output


if __name__ == "__main__":
    solution = Solution()
    s = ["abcabcbb", "bbbbb", "pwwkew", "dvdf"]
    output = [3, 1, 3, 3]

    for c in s:
        print("#", solution.lengthOfLongestSubstring(c))
