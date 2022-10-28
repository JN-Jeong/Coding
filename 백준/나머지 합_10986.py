"""
참고
https://zoosso.tistory.com/550

5 3
1 2 3 1 2

7
-------------
"""

# N, M = map(int, input().split())
# A = [0] + list(map(int, input().split())) # 런타임 에러(NameError) 발생함, 왜지?

# memo = [0] * M

# for i in range(N):
#     A[i+1] += A[i]
#     memo[A[i] % M] += 1

# print(A)
# print(memo)

# answer = memo[0]
# for i in range(len(memo)):
#     answer += memo[i] * (memo[i] - 1) // 2

# print(answer)

N, M = map(int, input().split())
A = list(map(int, input().split())) + [0]

memo = [0] * M

for i in range(N):
    A[i] += A[i - 1]
    memo[A[i] % M] += 1

print(A)
print(memo)

answer = memo[0]
for i in range(len(memo)):
    answer += memo[i] * (memo[i] - 1) // 2

print(answer)
