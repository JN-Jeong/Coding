"""
solved
"""


def solution(survey, choices):
    answer = ""
    surveys = dict()
    characters = ["R", "T", "C", "F", "J", "M", "A", "N"]
    for c in characters:
        dict.setdefault(surveys, c, 0)

    for i, c in enumerate(choices):
        score = abs(c - 1 - 3)
        if c < 4:  # 비동의 선택지
            surveys[survey[i][0]] += score
        elif c > 4:  # 동의 선택지
            surveys[survey[i][1]] += score

    for i in range(0, len(characters), 2):
        if surveys[characters[i]] < surveys[characters[i + 1]]:
            answer += characters[i + 1]
        else:
            answer += characters[i]

    return answer


if __name__ == "__main__":
    survey = [["AN", "CF", "MJ", "RT", "NA"], ["TR", "RT", "TR"]]
    choices = [[5, 3, 2, 7, 5], [7, 1, 3]]
    results = ["TCMA", "RCJA"]

    for i, data in enumerate(zip(survey, choices)):
        s, c = data
        print(solution(s, c))
