def solution():
    A, B, K = map(int, input().split())

    recul = []
    flag = True
    for i in range(1, K + 1):
        now = min((2**i * A) % (A + B), (-(2**i) * A) % (A + B))
        if i == 1:
            check = now
            recul.append(check)
        elif check == now:
            flag = False
            break
        else:
            recul.append(now)

    print(recul)
    print("@ : ", (K + 1) % len(recul))

    if flag:
        answer = now
    else:
        answer = recul[(K + 1) % len(recul)]

    return answer


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        print(f"#{i+1} {solution()}")
