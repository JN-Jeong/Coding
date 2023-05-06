def solution():
    N, Q = map(int, input().split())
    cows = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    temp = []
    for i in range(N):
        temp_S = 1
        for j in range(4):
            temp_S *= cows[(i + j) % N]
        temp.append(temp_S)
    print(temp)

    answer = sum(temp)
    print("@", answer)
    for num in nums:
        for i in range(num - 4, num):
            temp[i] = -temp[i]
            answer += 2 * temp[i]
            print("#", answer)
        print(answer)


if __name__ == "__main__":
    solution()
