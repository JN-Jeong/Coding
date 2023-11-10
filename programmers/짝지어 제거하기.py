"""
프로그래머스 : 짝지어 제거하기
"""


def solution(seqs):
    answer = 1
    stack = []
    for s in seqs:
        stack.append(s)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    if stack:
        answer = 0

    return answer


if __name__ == "__main__":
    seqs = ["baabaa", "cdcd", "aaaaa", "aaabbb"]
    result = [1, 0]

    for i, data in enumerate(seqs):
        s = data
        print(f"#{i}", solution(s))
