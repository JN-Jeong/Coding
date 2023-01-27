def solution(e, starts):
    answer = []
    divisor = [1 for _ in range(e + 1)]
    memo = 0
    starts_dict = {}
    sorted_starts = sorted(starts)

    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            divisor[j] += 1

    for i in range(len(sorted_starts)):
        if memo == 0:
            max_index = divisor[sorted_starts[i] :].index(max(divisor[sorted_starts[i] :])) + sorted_starts[i]
            starts_dict[sorted_starts[i]] = max_index
            memo = max_index
        else:
            if sorted_starts[i] <= memo:
                starts_dict[sorted_starts[i]] = memo
            else:
                memo = divisor[sorted_starts[i] :].index(max(divisor[sorted_starts[i] :])) + sorted_starts[i]
                starts_dict[sorted_starts[i]] = memo

        print(divisor)
        print(starts_dict)

    for s in starts:
        answer.append(starts_dict.get(s))

    return answer


if __name__ == "__main__":
    es = [8, 15]
    starts = [[1, 3, 7], [1, 3, 7]]
    result = [[6, 6, 8]]
    for e, start in zip(es, starts):
        print(solution(e, start))
