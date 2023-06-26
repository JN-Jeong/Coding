def solution(cap, n, deliveries, pickups):
    answer = 0
    delivers = 0
    picks = 0

    for i in range(n - 1, -1, -1):
        delivers += deliveries[i]
        picks += pickups[i]

        while delivers > 0 or picks > 0:
            delivers -= cap
            picks -= cap
            answer += (i + 1) * 2

    return answer


if __name__ == "__main__":
    caps = [4, 2]
    nums = [5, 7]
    deliveries = [[1, 0, 3, 1, 2], [1, 0, 2, 0, 1, 0, 2]]
    pickups = [[0, 3, 0, 4, 0], [0, 2, 0, 1, 0, 2, 0]]
    result = [16, 30]

    for c, n, delivery, pickup in zip(caps, nums, deliveries, pickups):
        print(solution(c, n, delivery, pickup))
