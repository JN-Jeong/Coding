def solution():
    string = input()

    global answer
    answer = [""] * len(string)

    def dfs(start, string):
        if not string:
            return

        global answer
        min_char = min(string)
        idx = string.index(min_char)

        answer[start + idx] = min_char
        print("".join(answer))
        dfs(start + idx + 1, string[idx + 1 :])
        dfs(start, string[:idx])

    dfs(0, string)


if __name__ == "__main__":
    solution()
