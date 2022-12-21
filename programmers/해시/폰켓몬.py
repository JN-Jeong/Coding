def solution(nums):
    answer = 0
    answer = min(len(nums) // 2, len(set(nums)))
    return answer


if __name__ == "__main__":
    nums = [[3, 1, 2, 3], [3, 3, 3, 2, 2, 4], [3, 3, 3, 2, 2, 2]]
    result = [2, 3, 2]
    for num in nums:
        print(solution(num))
