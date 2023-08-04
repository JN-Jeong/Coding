"""
3. Longest Substring Without Repeating Characters
"""

from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        temp = [""] * numRows
        idx, step = 0, 1

        for c in s:
            temp[idx] += c
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
            # print(temp)

        return "".join(temp)


if __name__ == "__main__":
    solution = Solution()
    s = ["PAYPALISHIRING", "PAYPALISHIRING", "A"]
    numRows = [3, 4, 1]
    output = ["PAHNAPLSIIGYIR", "PINALSIGYAHRPI", "A"]

    for c, r in zip(s, numRows):
        print("#", solution.convert(c, r))
