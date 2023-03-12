from collections import defaultdict


def solution():
    N, X = map(int, input().split())
    visitors = list(map(int, input().split()))

    cumsum = [0]
    for n in visitors:
        cumsum.append(cumsum[-1] + n)

    visits = defaultdict(int)
    answer = 0
    for i in range(X, N + 1):
        temp = cumsum[i] - cumsum[i - X]
        answer = max(answer, temp)
        visits[temp] += 1

    if answer == 0:
        print("SAD")
    else:
        print(answer)
        print(visits[answer])


if __name__ == "__main__":
    solution()
