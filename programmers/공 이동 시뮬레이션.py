def solution(n, m, x, y, queries):
    answer = 0

    top, bottom, left, right = x, x, y, y

    for i in range(len(queries) - 1, -1, -1):
        dir, repeat = queries[i]

        if dir == 0:  # 왼쪽으로
            if right + repeat < m:
                temp = right + repeat
            else:
                temp = m - 1

            if left == 0:
                right = temp
            else:
                left, right = left + repeat, temp

        if dir == 1:  # 오른쪽으로
            if left - repeat >= 0:
                temp = left - repeat
            else:
                temp = 0

            if right == m - 1:
                left = temp
            else:
                left, right = temp, right - repeat

        if dir == 2:  # 위로
            if bottom + repeat < n:
                temp = bottom + repeat
            else:
                temp = n - 1

            if top == 0:
                bottom = temp
            else:
                top, bottom = top + repeat, temp

        if dir == 3:  # 아래로
            if top - repeat >= 0:
                temp = top - repeat
            else:
                temp = 0

            if bottom == n - 1:
                top = temp
            else:
                top, bottom = temp, bottom - repeat

        if left > m - 1 or right < 0 or top > n - 1 or bottom < 0:
            break

    else:
        answer = ((bottom - top) + 1) * ((right - left) + 1)

    return answer


if __name__ == "__main__":
    ns = [2, 2, 1000]
    ms = [2, 5, 1000]
    xs = [0, 0, 1]
    ys = [0, 1, 1]
    queries = [[[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]], [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]], [[0, 100001], [2, 100001]]]
    result = [4, 2]
    for n, m, x, y, query in zip(ns, ms, xs, ys, queries):
        print(solution(n, m, x, y, query))
