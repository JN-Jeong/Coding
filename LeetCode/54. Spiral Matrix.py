"""
54. Spiral Matrix
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        row = len(matrix)
        col = len(matrix[0])
        visited = [[0] * col for _ in range(row)]

        tr = row // 2
        tc = col // 2
        print("@", tr, tc)

        # 우하좌상
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        d = 0  # 회전 방향
        y = 0  # row 좌표
        x = 0  # col 좌표
        while True:
            answer.append(matrix[y][x])
            if len(answer) == row * col:
                break

            visited[y][x] = 1
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < row and 0 <= nx < col and visited[ny][nx] == 0:
                y = ny
                x = nx
            else:
                d = (d + 1) % 4
                y = y + dy[d]
                x = x + dx[d]
            print(y, x)

        return answer


if __name__ == "__main__":
    solution = Solution()
    matrics = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[6, 9, 7]]]
    output = [[1, 2, 3, 6, 9, 8, 7, 4, 5], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], [6, 9, 7]]

    for m in matrics:
        print("#", solution.spiralOrder(m))
