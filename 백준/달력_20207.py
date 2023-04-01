def solution():
    answer = 0
    N = int(input())

    schedule = [0] * 366
    ids = []
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E + 1):
            schedule[i] += 1
    print(schedule)

    series = False
    idx = 0
    while idx < len(schedule):
        temp = []
        row = 0
        if series == False and schedule[idx] > 0:
            temp.append(idx)
            while idx < len(schedule) and schedule[idx] > 0:
                print(idx)
                row = max(row, schedule[idx])
                idx += 1
            temp.append(idx - 1)
            temp.append(row)
            ids.append(temp)
        idx += 1
    print(ids)

    for idx in ids:
        s, e, r = idx
        answer += (e - s + 1) * r
    print(answer)


if __name__ == "__main__":
    solution()
