"""
택배상자
"""
# from collections import deque


# def solution(order):
#     answer = 0

#     n = len(order)
#     boxes = deque([i + 1 for i in range(n)])
#     stack = []
#     for i in range(n):
#         box = order[i]

#         if stack:
#             if stack[-1] == box:
#                 stack.pop()
#                 answer += 1
#             else:
#                 if boxes:
#                     while boxes:
#                         b = boxes.popleft()
#                         if b == box:
#                             answer += 1
#                             break

#                         stack.append(b)
#                 else:
#                     break
#         else:
#             while boxes:
#                 b = boxes.popleft()
#                 if b == box:
#                     answer += 1
#                     break

#                 stack.append(b)

#     return answer


def solution(order):
    answer = 0

    n = len(order)
    stack = []
    for i in range(n):
        stack.append(i + 1)

        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer += 1

    return answer


if __name__ == "__main__":
    order = [[4, 3, 1, 2, 5], [5, 4, 3, 2, 1], [4, 5, 1, 2, 3], [4, 5, 3, 2, 1]]
    answer = [2, 5]

    for i, data in enumerate(order):
        o = data
        print(f"#{i}", solution(o))
