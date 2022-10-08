def solution(sizes):
    answer = 0

    max_row = 0
    max_col = 0
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        max_row = max(max_row, size[0])
        max_col = max(max_col, size[1])

    answer = max_row * max_col
    return answer


sizes = [[[60, 50], [30, 70], [60, 30], [80, 40]], [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]], [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]]
result = [4000, 120, 133]

for size in sizes:
    print(solution(size))
