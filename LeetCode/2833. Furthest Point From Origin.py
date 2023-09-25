"""
2833. Furthest Point From Origin
"""

from typing import List


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        underline = 0
        answer = 0
        for c in moves:
            if c == "L":
                answer -= 1
            elif c == "R":
                answer += 1
            else:
                underline += 1

        answer = abs(answer) + underline

        return answer


if __name__ == "__main__":
    solution = Solution()
    moves = ["L_RL__R", "_R__LL_", "_______"]
    output = [3, 5, 7]

    for m in moves:
        print("#", solution.furthestDistanceFromOrigin(m))
