def solution():
    N, K = map(int, input().split())
    distances = list(map(int, input().split()))
    sum_dis = [0]
    for d in distances:
        sum_dis.append(sum_dis[-1] + d)
    print(sum_dis)

    total = sum(distances)
    if K > total:
        K -= total
        K = total - K
    print(K)

    for i in range(N):
        if sum_dis[i] <= K < sum_dis[i + 1]:
            answer = i + 1
            break

    print(answer)


if __name__ == "__main__":
    solution()
