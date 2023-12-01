"""
Summer/Winter Coding(~2018)
스킬트리
"""
import re


def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        st = re.sub(rf"[^{skill}]", "", st)

        for a, b in zip(skill, st):
            if a != b:
                break

        else:
            answer += 1

    return answer


# def solution(skill, skill_trees):
#     answer = 0

#     for skills in skill_trees:
#         skill_list = list(skill)

#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1

#     return answer


if __name__ == "__main__":
    skills = ["CBD"]
    skill_trees = [["BACDE", "CBADF", "AECB", "BDA"]]

    answer = [2]

    for i, data in enumerate(zip(skills, skill_trees)):
        s, st = data
        print(f"#{i}", solution(s, st))
