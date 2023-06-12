def solution():
    answer = 0
    strings = input()

    stack = []
    temp = 1

    idx = 0
    for idx in range(len(strings)):
        string = strings[idx]
        if string == "(":
            temp *= 2
            stack.append("(")
        elif string == "[":
            temp *= 3
            stack.append("[")

        if string == ")":
            if stack:
                s = stack.pop()
            else:
                return 0

            if s == "[":
                return 0

            if strings[idx - 1] == "(":
                answer += temp
            temp //= 2

        elif string == "]":
            if stack:
                s = stack.pop()
            else:
                return 0

            if s == "(":
                return 0

            if strings[idx - 1] == "[":
                answer += temp
            temp //= 3

        idx += 1

        # print(f"answer : {answer}, string : {string}, temp : {temp}, stack : {stack}")

    if stack:
        return 0

    return answer


if __name__ == "__main__":
    print(solution())
