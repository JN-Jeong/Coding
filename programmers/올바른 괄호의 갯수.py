"""
프로그래머스 : 올바른 괄호의 갯수
"""


# def solution(n):
#     global answer
#     answer = 0

#     def check(brackets):
#         stack = []
#         for b in brackets:
#             if b == "(":
#                 stack.append(b)
#             elif stack:
#                 stack.pop()
#             else:
#                 return False

#         if stack:
#             return False
#         return True

#     def recur(brackets, left, right):
#         global answer
#         if left > n:
#             return
#         if right > n - 1:
#             return
#         if len(brackets) == n * 2 - 1:
#             if check(brackets + ")"):
#                 answer += 1
#             return

#         recur(brackets + "(", left + 1, right)
#         recur(brackets + ")", left, right + 1)

#     recur("(", 1, 0)

#     return answer


def solution(n):
    memo = [[], ["()"]]
    brackets = [[]]
    for i in range(1, n + 1):
        kinds = []
        for j in range(1, i + 1):
            for k in range(1, i - j + 1):
                if j + k == i:
                    kinds.append((j, k))
        brackets.append(kinds)
    print("@", brackets)

    for i in range(2, n + 1):
        temp = []
        for l in memo[i - 1]:
            temp.append("(" + l + ")")
        for j, k in brackets[i]:
            for t1 in memo[j]:
                for t2 in memo[k]:
                    temp.append(t1 + t2)
        memo.append(list(set(temp)))
    print("@@", memo)

    return len(memo[n])


# def solution(n):
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     for i in range(1, n + 1):
#         for j in range(i):
#             dp[i] += dp[j] * dp[i - j - 1]

#     return dp[n]


if __name__ == "__main__":
    n = [2, 3]
    results = [2, 5]

    for i, data in enumerate(n):
        d = data
        print(f"#{i}", solution(d))
