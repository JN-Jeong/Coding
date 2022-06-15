"""
5
-2 4 -99 -1 98
5
-2 1 -99 -1 98
10
1 2 3 4 5 -6 -7 -8 -9 -10
"""

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
print(solutions)

left = 0
right = N-1
min_ = abs(solutions[left] + solutions[right])
result = [solutions[left], solutions[right]]

while left < right:
    s_left = solutions[left]
    s_right = solutions[right]
    tot = s_left + s_right

    if abs(tot) < min_:
        min_ = abs(tot)
        result = [s_left, s_right]

    if tot < 0:
        left += 1
    else:
        right -= 1
    print(min_)

print(result[0], result[1])