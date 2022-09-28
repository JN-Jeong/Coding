def solution(nums, losts, reserves):
    answer = 0

    clothes = [1] * nums
    for lost in losts:
        clothes[lost - 1] -= 1
    for reserve in reserves:
        clothes[reserve - 1] += 1

    for i in range(nums):
        if clothes[i] == 2:
            if i == 0:
                if clothes[i + 1] == 0:
                    clothes[i + 1] += 1
                    clothes[i] -= 1
            elif i == nums - 1:
                if clothes[i - 1] == 0:
                    clothes[i - 1] += 1
                    clothes[i] -= 1
            else:
                if clothes[i - 1] == 0:
                    clothes[i - 1] += 1
                    clothes[i] -= 1
                elif clothes[i + 1] == 0:
                    clothes[i + 1] += 1
                    clothes[i] -= 1
    print(clothes)

    for i in clothes:
        if i > 0:
            answer += 1
    return answer


nums = [5, 5, 3]
losts = [
    [2, 4],
    [2, 4],
    [3],
]
reserves = [[1, 3, 5], [3], [1]]
results = [5, 4, 2]

for n, lost, reserve in zip(nums, losts, reserves):
    print(solution(n, lost, reserve))
