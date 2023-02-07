from collections import deque


def solution():
    answer = []
    N = int(input())
    nums = deque(enumerate(map(int, input().split())))

    while nums:
        idx, num = nums.popleft()
        answer.append(idx + 1)
        if num > 0:
            nums.rotate(-(num - 1))
        elif num < 0:
            nums.rotate(-num)

    return answer


if __name__ == "__main__":
    for i in solution():
        print(i, end=" ")
