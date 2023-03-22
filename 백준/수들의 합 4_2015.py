from collections import defaultdict


def solution():
    answer = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[-1] + A[i])
    cumsum = cumsum[1:]

    prefix = defaultdict(int)

    for i in range(N):
        if cumsum[i] == K:
            answer += 1
        answer += prefix[cumsum[i] - K]
        prefix[cumsum[i]] += 1
        print(prefix, answer)

    print(cumsum)
    print(answer)


if __name__ == "__main__":
    solution()
