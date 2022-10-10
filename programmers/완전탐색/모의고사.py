def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    p1 = p1 * int(round(len(answers) / len(p1), 0) + 1)
    p2 = p2 * int(round(len(answers) / len(p2), 0) + 1)
    p3 = p3 * int(round(len(answers) / len(p3), 0) + 1)

    # print(p1, p2, p3)

    s = [0, 0, 0]

    for i in range(len(answers)):
        if p1[i] == answers[i]:
            s[0] += 1
        if p2[i] == answers[i]:
            s[1] += 1
        if p3[i] == answers[i]:
            s[2] += 1

    max_ = max(s)
    for i, score in enumerate(s):
        if score == max_:
            answer.append(i + 1)

    return answer


answers = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]
returns = [[1], [1, 2, 3]]

for answer in answers:
    print(solution(answer))
