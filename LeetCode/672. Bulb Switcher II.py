"""
672. Bulb Switcher II
"""

from typing import List

# class Solution:
#     def flipLights(self, n: int, presses: int) -> int:
#         answer = []

#         def recur(cnt, pressed):
#             if cnt == presses:
#                 bulbs = [1] * n
#                 for p in pressed:
#                     if p == 1:  # 모든 전구 뒤집기
#                         for i in range(n):
#                             bulbs[i] = (bulbs[i] + 1) % 2

#                     if p == 2:  # 짝수번째 전구 뒤집기
#                         for i in range(1, n, 2):
#                             bulbs[i] = (bulbs[i] + 1) % 2

#                     if p == 3:  # 홀수번째 전구 뒤집기
#                         for i in range(0, n, 2):
#                             bulbs[i] = (bulbs[i] + 1) % 2

#                     if p == 4:  # j = 3k + 1 전구 뒤집기
#                         for i in range(n):
#                             idx = i * 3
#                             if idx >= len(bulbs):
#                                 continue
#                             bulbs[idx] = (bulbs[idx] + 1) % 2

#                 if bulbs not in answer:
#                     answer.append(bulbs)
#                 return

#             for i in range(1, 5):
#                 recur(cnt + 1, pressed + [i])

#         recur(0, [])

#         # print(answer)
#         return len(answer)


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2 and presses == 1:
            return 3
        if n == 2:
            return 4
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        if presses >= 3:
            return 8
        return 8


if __name__ == "__main__":
    solution = Solution()
    ns = [1, 2, 3, 4]
    presses = [1, 1, 1, 1]
    output = [2, 3, 4, 4]

    for i, data in enumerate(zip(ns, presses)):
        n, p = data
        print(f"#{i}", solution.flipLights(n, p))
