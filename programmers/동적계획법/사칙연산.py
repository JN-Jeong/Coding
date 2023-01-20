def solution(arr):
    answer = -1

    result = [0, 0]  # min, max
    total = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == "+":
            continue

        elif arr[i] == "-":
            total_min, total_max = result
            result[0] = min(-(total + total_max), -total + total_min)

            minus_v = int(arr[i + 1])
            result[1] = max(-(total + total_min), -minus_v + (total - minus_v) + total_max)

            total = 0

        elif int(arr[i]) >= 0:
            total += int(arr[i])

    result[1] += total
    answer = result[1]

    return answer


arrs = [["1", "-", "3", "+", "5", "-", "8"], ["5", "-", "3", "+", "1", "+", "2", "-", "4"]]
result = [1, 3]

for arr in arrs:
    print(solution(arr))
