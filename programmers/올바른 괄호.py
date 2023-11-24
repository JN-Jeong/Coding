"""
프로그래머스 : 올바른 괄호
"""


def solution(brackets):
    stack = []

    for s in brackets:
        if stack and s == ")":
            stack.pop()
        elif s == "(":
            stack.append("(")
        else:
            return False

    if stack:
        return False
    return True


if __name__ == "__main__":
    brackets = ["()()", "(())()", ")()(", "(()("]
    result = [29, 10]

    for i, data in enumerate(brackets):
        s = data
        print(f"#{i}", solution(s))
