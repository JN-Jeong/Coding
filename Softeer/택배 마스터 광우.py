"""
https://softeer.ai/practice/6273
택배 마스터 광우
"""

import sys
from itertools import permutations


def solution():
    answer = float("inf")
    N, M, K = map(int, input().split())
    rails = list(map(int, input().split()))

    permu_rails = list(permutations(rails, N))
    for rail in permu_rails:
        result = 0
        cnt = 0
        for _ in range(K):
            weight = 0

            while True:
                weight += rail[cnt]
                cnt = (cnt + 1) % N
                if weight + rail[cnt] > M:  # 다음 택배를 담았을 때 바구니 무게(M)를 초과하면 break
                    break

            result += weight

        answer = min(answer, result)

    return answer


if __name__ == "__main__":
    print(solution())
