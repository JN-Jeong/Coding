"""
프로그래머스 : 뒤에 있는 큰 수 찾기
"""


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    print(stack)
    return answer


if __name__ == "__main__":
    numbers = [[2, 3, 3, 5], [9, 1, 5, 3, 6, 2]]
    result = [[3, 5, 5, -1], [-1, 5, 6, 6, -1, -1]]

    for i, n in enumerate(numbers):
        print(f"#{i}", solution(n))
