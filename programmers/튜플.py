"""
2019 카카오 개발자 겨울 인턴십
튜플
"""
# import re
# from collections import Counter


# def solution(s):
#     s = Counter(re.findall("\d+", s))
#     return list(
#         map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)])
#     )


def solution(s):
    answer = []

    arr = s[2:-2].split("},{")
    arr.sort(key=lambda x: len(x))
    print("@", arr)

    for a in arr:
        temp = list(map(int, a.split(",")))
        for t in temp:
            if t not in answer:
                answer.append(t)

    return answer


if __name__ == "__main__":
    inputs = [
        "{{2},{2,1},{2,1,3},{2,1,3,4}}",
        "{{1,2,3},{2,1},{1,2,4,3},{2}}",
        "{{20,111},{111}}",
        "{{123}}",
        "{{4,2,3},{3},{2,3,4,1},{2,3}}",
    ]

    answer = [[2, 1, 3, 4], [2, 1, 3, 4], [111, 20], [123], [3, 2, 4, 1]]

    for i, data in enumerate(inputs):
        s = data
        print(f"#{i}", solution(s))
