# def solve(form, n):
#     if n == N:
#         if eval(form.replace(' ', '')) == 0:
#             print(form)
#             return form
#         return

#     # ASCII 순서 맞춰줘야함
#     solve(form + ' ' + str(n+1), n+1)
#     solve(form + '+' + str(n+1), n+1)
#     solve(form + '-' + str(n+1), n+1)


# T = int(input())

# for i in range(T):
#     N = int(input())
#     solve('1', 1)
#     print()


# eval X
# 수식, 다음 수열 값, 연산자, 이어 붙인 값(계산 할 값), 현재까지의 계산 결과
def solve(form, n, concat_n, oper, result):
    if n == N:
        result = result + (oper * concat_n)
        # print(result)
        if result == 0:
            print(form)
            return
    else:
        # ASCII 순서 맞춰줘야함 (공백, +, -(32, 43, 45) 순으로)
        solve(form + " " + str(n + 1), n + 1, concat_n * 10 + n + 1, oper, result)
        solve(form + "+" + str(n + 1), n + 1, n + 1, 1, result + oper * concat_n)
        solve(form + "-" + str(n + 1), n + 1, n + 1, -1, result + oper * concat_n)


T = int(input())

for i in range(T):
    N = int(input())
    solve("1", 1, 1, 1, 0)
    print()


# # 패캠 강의 풀이
# import copy

# def recur(array, n):
#     if len(array) == n:
#         operators_list.append(copy.deepcopy(array))
#         return

#     array.append(' ')
#     recur(array, n)
#     array.pop()

#     array.append('+')
#     recur(array, n)
#     array.pop()

#     array.append('-')
#     recur(array, n)
#     array.pop()

# test_case = int(input())

# for _ in range(test_case):
#     operators_list = []
#     n = int(input())
#     recur([], n - 1)

#     integers = [i for i in range(1, n+1)]

#     for operators in operators_list:
#         string = ''
#         for i in range(n - 1):
#             string += str(integers[i]) + operators[i]
#         string += str(integers[-1])
#         if eval(string.replace(' ', '')) == 0:
#             print(string)
#     print()
