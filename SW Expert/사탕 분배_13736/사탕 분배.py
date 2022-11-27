def solution():
    A, B, K = map(int, input().split())

    candies = [A, B]
    recul = []
    flag = True
    for i in range(K):
        if candies[0] < candies[1]:  # B가 사탕이 더 많음
            candies[0], candies[1] = candies[0] * 2, candies[1] - candies[0]
        else:  # A가 사탕이 더 많음
            candies[1], candies[0] = candies[1] * 2, candies[0] - candies[1]
        # print(candies)

        now = min(candies)
        if i == 0:
            check = now
            recul.append(check)
        elif check == now:
            flag = False
            break
        else:
            recul.append(now)
    # print(recul)
    # print((K + 1) % len(recul))
    if flag:
        answer = now
    else:
        answer = recul[(K + 1) % len(recul)]

    return answer


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        print(f"#{i+1} {solution()}")
