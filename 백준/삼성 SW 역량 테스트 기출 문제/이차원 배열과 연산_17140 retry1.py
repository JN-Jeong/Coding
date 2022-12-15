def solution():
    answer = 0
    r, c, k = map(int, input().split())
    r = r - 1
    c = c - 1
    A = [list(map(int, input().split())) for _ in range(3)]

    # for a in A:
    #     print(a)
    # print()

    row_len, col_len = 3, 3
    while answer < 100 + 1:
        if r < row_len and c < col_len and A[r][c] == k:
            break

        for a in A:
            print(a)
        print()

        # R연산 후에는 col_len(열의 개수)가 변화하고 C연산 후에는 row_len(행의 개수)가 변화함
        if row_len >= col_len:  # R연산
            A, col_len = sort_(A, col_len)  # col_len 갱신
        else:  # C연산
            A, row_len = sort_(list(zip(*A)), row_len)  # row_len 갱신
            A = list(zip(*A))  # 2차원 행렬 transpose

        answer += 1

    else:
        return -1

    # board, len_ = sort_(A, 3)
    # for b in board:
    #     print(b)
    # print()

    return answer


def sort_(A: list, max_len: int):  # max_len : A의 최대 행 또는 열 길이
    for idx, row in enumerate(A):
        nums = []
        for n in set(row):
            if n:
                nums.append((n, row.count(n)))

        # print(nums)
        nums = sorted(nums, key=lambda x: [x[1], x[0]])
        len_nums = len(nums)
        if len_nums > 50:  # nums가 (숫자, 개수)로 이루어져있음
            len_nums = 50
        max_len = max(max_len, len_nums * 2)  # row 또는 column의 최대 길이

        # 정렬한 결과 추가
        A[idx] = []
        for i in range(len_nums):
            A[idx].append(nums[i][0])
            A[idx].append(nums[i][1])

    # 패딩
    for idx, row in enumerate(A):
        for _ in range(max_len - len(row)):
            A[idx].append(0)

    return A, max_len


if __name__ == "__main__":
    print(solution())
