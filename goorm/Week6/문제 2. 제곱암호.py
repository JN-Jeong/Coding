# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    alphabet_dict = {}
    num_dict = {}
    for i, a in enumerate(alphabet.split()):
        alphabet_dict[a] = i
        num_dict[i] = a
    # print(alphabet_dict)
    # print(num_dict)

    N = int(input())
    S = input()

    answer = ""
    for i in range(0, N, 2):
        idx = int(S[i + 1]) ** 2 % 26
        answer += num_dict[(alphabet_dict[S[i]] + idx) % 26]

    return answer


if __name__ == "__main__":
    print(solution())
