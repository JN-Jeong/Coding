def solution():
    N = input()

    def is_odd(num):
        if int(num) % 2 == 0:
            return False
        return True

    global answer_max, answer_min
    answer_max = 0
    answer_min = float("inf")

    answer = 0
    for n in N:
        if is_odd(n):
            answer += 1

    def recul(N, answer):
        global answer_max, answer_min
        # print(N)
        if len(N) >= 3:
            for n in N:
                if is_odd(n):
                    answer += 1

            for i in range(1, len(N) - 1):
                for j in range(i + 1, len(N)):
                    recul(str(int(N[:i]) + int(N[i:j]) + int(N[j:])), answer)

        elif len(N) >= 2:
            if is_odd(N[0]):
                answer += 1
            if is_odd(N[1]):
                answer += 1
            N = str(int(N[0]) + int(N[1]))
            recul(N, answer)

        elif len(N) == 1:
            if is_odd(N):
                answer += 1
            answer_max = max(answer_max, answer)
            answer_min = min(answer_min, answer)
            return

    recul(N, 0)

    print(answer_min, answer_max)


if __name__ == "__main__":
    solution()
