import re


def solution():
    S = input()
    # print(re.findall(r"< ?.*? ?>|[a-z0-9 ]+", S))
    # print(re.split(r"< ?.*? ?>", S))
    answer = ""
    for w in re.findall(r"< ?.*? ?>|[a-z0-9 ]+", S):
        if "<" in w and ">" in w:
            answer += w
        else:
            temp = ""
            for c in w.split():
                temp += c[::-1] + " "
            answer += temp.strip()

    print(answer)


if __name__ == "__main__":
    solution()
