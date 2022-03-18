from random import randrange


T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    results = []
    sum = 0
    for j in range(len(A) - M + 1):
        for k in range(M):
            sum += A[j + k]
        results.append(sum)
        sum = 0

    result = max(results) - min(results)
    print("#{} {}".format(i+1, result))