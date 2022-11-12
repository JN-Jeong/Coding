"""
2
5 6
0 0 1 0
"""

N = int(input())
A = list(map(int, input().split()))
opers = list(map(int, input().split()))

# opers[0] : 덧셈 개수
# opers[1] : 뺄셈 개수
# opers[2] : 곱셈 개수
# opers[3] : 나눗셈 개수

maximum = -9876543210
minimum = 9876543210
def solve(idx, res, plus, minus, multiply, divide):
    global maximum, minimum

    if idx == N:
        maximum = max(res, maximum)
        minimum = min(res, minimum)
        return
    
    if plus:
        solve(idx + 1, res + A[idx], plus - 1, minus, multiply, divide)
    if minus:
        solve(idx + 1, res - A[idx], plus, minus - 1, multiply, divide)
    if multiply:
        solve(idx + 1, res * A[idx], plus, minus, multiply - 1, divide)
    if divide:
        solve(idx + 1, int(res / A[idx]), plus, minus, multiply, divide - 1)

solve(1, A[0], opers[0], opers[1], opers[2], opers[3])
print(maximum)
print(minimum)