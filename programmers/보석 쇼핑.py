"""
2020 카카오 인턴십
보석 쇼핑
"""


def solution(gems):
    answer = [0, len(gems)]
    N = len(set(gems))
    left, right = 0, 0
    dict_gems = {gems[0]: 1}

    while left < len(gems) and right < len(gems):
        if len(dict_gems) == N:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:  # left를 오른쪽으로 이동(보석 삭제)
                dict_gems[gems[left]] -= 1
                if dict_gems[gems[left]] == 0:
                    del dict_gems[gems[left]]
                left += 1

        else:  # right를 오른쪽으로 이동(보석 추가)
            right += 1
            if right == len(gems):
                break

            dict_gems[gems[right]] = dict_gems.get(gems[right], 0) + 1

    answer = [answer[0] + 1, answer[1] + 1]
    return answer


if __name__ == "__main__":
    gems = [
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
        ["AA", "AB", "AC", "AA", "AC"],
        ["XYZ", "XYZ", "XYZ"],
        ["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
    ]
    answer = [[3, 7], [1, 3], [1, 1], [1, 5]]

    for i, data in enumerate(gems):
        gem = data
        print(f"#{i}", solution(gem))
