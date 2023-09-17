"""
solved
"""


def solution(arr):
    stack = []

    i = 0
    while i < len(arr):
        if stack:
            if stack[-1] < arr[i]:
                stack.append(arr[i])
                i += 1
            elif stack[-1] >= arr[i]:
                stack.pop()
        else:
            stack.append(arr[i])
            i += 1

    return stack


if __name__ == "__main__":
    arr = [[1, 4, 2, 5, 3]]
    results = [[1, 2, 3]]
    for inputs in arr:
        print(solution(inputs))
