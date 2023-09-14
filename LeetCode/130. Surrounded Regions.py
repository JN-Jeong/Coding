"""
209. Minimum Size Subarray Sum
"""

from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]) and board[i][j] == "O":
                    q.append([i, j])

        # 상좌하우
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]

        while q:
            y, x = q.popleft()
            board[y][x] = "."

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == "O":
                    q.append([ny, nx])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        for b in board:
            print(b)


if __name__ == "__main__":
    solution = Solution()
    inputs = [[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]], [["X"]]]
    output = [[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]], [["X"]]]

    for i, data in enumerate(inputs):
        a = data
        print(f"#{i}", solution.solve(a))
