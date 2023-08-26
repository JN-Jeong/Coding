"""
74. Search a 2D Matrix
"""

from typing import List, Optional

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         row = len(matrix) + 1
#         for i, rows in enumerate(matrix):
#             if target <= rows[-1]:
#                 row = i
#                 break

#         if row > len(matrix):
#             return False

#         for n in matrix[row]:
#             if n == target:
#                 return True
#         return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix[0]), len(matrix)
        s, e = 0, row * col - 1
        while s < e:
            mid = (s + e) // 2
            if matrix[mid // row][mid % row] < target:
                s = mid + 1
            else:
                e = mid
        return matrix[s // row][s % row] == target


if __name__ == "__main__":
    solution = Solution()
    matrices = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], [[1]]]
    targets = [3, 13, 2]
    output = [True, False]

    for matrix, t in zip(matrices, targets):
        print("#", solution.searchMatrix(matrix, t))
