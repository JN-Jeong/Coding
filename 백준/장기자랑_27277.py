def solution():
    N = int(input())
    array = list(map(int, input().split()))
    array = sorted(array, reverse=True)
    # print(array)

    answer = array[0]
    temp = []
    for i in range(N // 2):
        temp.append(array[i])
        temp.append(array[-(i + 1)])
    if N % 2 != 0:
        temp.append(array[N // 2])
    # print(temp)

    for i in range(N - 1):
        answer += max(0, temp[i + 1] - temp[i])

    print(answer)


if __name__ == "__main__":
    solution()

"""
6 1 5 2 4 3
6 0 4 0 2 0
"""
