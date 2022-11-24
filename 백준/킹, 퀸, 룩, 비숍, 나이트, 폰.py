def solution(pieces):
    sets = [1, 1, 2, 2, 2, 8]
    result = []
    for i in range(len(sets)):
        result.append(str(sets[i] - pieces[i]))

    return " ".join(result)


if __name__ == "__main__":
    pieces = [[0, 1, 2, 2, 2, 7], [2, 1, 2, 1, 2, 1]]
    results = [[1, 0, 0, 0, 0, 1], [-1, 0, 0, 1, 0, 7]]

    # for p in pieces:
    #     print(solution(p))

    pieces = list(map(int, input().split()))
    print(solution(pieces))
