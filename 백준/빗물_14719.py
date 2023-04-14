def solution():
    H, W = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = 0

    for i in range(1, W - 1):
        left_max = max(heights[:i])
        right_max = max(heights[i + 1 :])

        wall = min(left_max, right_max)

        if heights[i] < wall:
            answer += wall - heights[i]

    print(answer)


if __name__ == "__main__":
    solution()
