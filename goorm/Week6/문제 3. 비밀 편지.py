# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    T = int(input())

    for _ in range(T):
        answer = ""
        S = input().rstrip()
        type_, token = input().split()

        token *= len(S) // len(token) + 1
        print(token)
        # print(chr(65), type_, token)
        # print(ord("A"))
        for i in range(len(S)):
            if S[i].isalpha():
                temp = ord(S[i])
                if 65 <= temp <= 90:
                    temp -= 65
                    if type_ == "E":
                        temp = int(temp + ord(token[i])) % 26 + 65
                    else:
                        temp = int(temp - ord(token[i])) % 26 + 65
                elif 97 <= temp <= 122:
                    temp -= 97
                    if type_ == "E":
                        temp = int(temp + ord(token[i])) % 26 + 97
                    else:
                        temp = int(temp - ord(token[i])) % 26 + 97

                answer += chr(temp)
            else:
                answer += S[i]
        print(answer)


if __name__ == "__main__":
    solution()
