def solution():
    answer = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = input()

    # i = 0
    # while i < len(string):
    #     j = 0
    #     if string[i] == "a":
    #         while j < len(alphabet) and i < len(string):
    #             if string[i] == alphabet[j]:
    #                 answer += 1
    #                 j += 1
    #                 i += 1
    #             else:
    #                 break
    #     else:
    #         i += 1

    if string[0] == "a":
        for i in range(len(string)):
            if string[i] == alphabet[i]:
                answer += 1
            else:
                break
    else:
        return 0

    return answer


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        print(f"#{i+1} {solution()}")
