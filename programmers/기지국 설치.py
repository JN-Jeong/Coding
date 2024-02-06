"""
Summer/Winter Coding(~2018)
기지국 설치
"""
import math


def solution(n, stations, w):
    answer = 0
    dist = []
    dist.append(stations[0] - w - 1)
    for i in range(1, len(stations)):
        dist.append((stations[i] - w - 1) - (stations[i - 1] + w))
    dist.append(n - (stations[-1] + w))
    # print("@", arr)

    for a in dist:
        answer += math.ceil(a / (2 * w + 1))

    return answer


if __name__ == "__main__":
    Ns = [11, 16, 200000000]
    stations = [[4, 11], [9], [3]]
    Ws = [1, 2, 1]
    answer = [3, 3]

    for i, data in enumerate(zip(Ns, stations, Ws)):
        n, station, w = data
        print(f"#{i}", solution(n, station, w))
