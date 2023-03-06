def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # print(*sorted(A + B))

    a_pointer = 0
    b_pointer = 0
    answer = []

    while a_pointer != N or b_pointer != M:
        if a_pointer == N:
            answer.append(B[b_pointer])
            b_pointer += 1
        elif b_pointer == M:
            answer.append(A[a_pointer])
            a_pointer += 1
        else:
            if A[a_pointer] < B[b_pointer]:
                answer.append(A[a_pointer])
                a_pointer += 1
            else:
                answer.append(B[b_pointer])
                b_pointer += 1

    print(*answer)


if __name__ == "__main__":
    solution()
