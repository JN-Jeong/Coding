def solution(brown, yellow):
    answer = []

    # brown => x * y - yellow
    # yellow => (x-2) * (y-2)
    # x = (brown+yellow) // y, y

    total = brown + yellow
    # for x in range((total)//2):
    #     for y in range((total)//2):
    #         if x * y - yellow == brown and (x-2) * (y-2) == yellow and x >= y:
    #             answer.append(x)
    #             answer.append(y)

    for y in range(3, int(total**0.5) + 1):
        if total % y == 0 and yellow == (y - 2) * (total // y - 2):
            answer.append(total // y)
            answer.append(y)

    return answer


browns = [10, 8, 24]
yellows = [2, 1, 24]
returns = [[4, 3], [3, 3], [8, 6]]

for brown, yellow in zip(browns, yellows):
    print(solution(brown, yellow))
