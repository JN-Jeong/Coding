from itertools import permutations


def solution():
    answer = "NIE"
    N = int(input())
    flies = []

    for _ in range(N):
        flies.append(list(map(int, input().split())))
    print(flies)

    indice = list(permutations(range(len(flies)), 2))
    print(indice)

    for idx1, idx2 in indice:
        normal_vector = cross_product(flies[idx1], flies[idx2])
        print("@ : ", normal_vector)

        if normal_vector in flies:
            return "TAK"

    return answer


def cross_product(vector1, vector2):  # 법선 벡터 (normal vector)
    return [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0],
    ]


if __name__ == "__main__":
    TC = int(input())

    for _ in range(TC):
        print(solution())
