# """
# 10 15
# 5 1 3 5 10 7 4 9 2 8

# 10 7
# 5 1 3 5 10 7 4 9 2 8

# 10 6
# 5 1 3 5 10 7 4 9 2 8

# 10 10
# 5 1 3 5 10 7 4 9 2 8

# 10 101
# 5 1 3 5 10 7 4 9 2 8

# 100 20
# 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 5 1 3 5 10 7 4 9 2 8 
# """

# N, S = map(int, input().split())
# sequences = list(map(int, input().split()))
# print(sequences)

# left = 0
# right = 0
# sum_ = 0
# result = N+1
# """
# 이건 왜 안되는거지?
# right index가 N값이 되어도 left 값을 줄여나가면서 최소가 되는 부분합을 찾아야 최종 답을 찾을 수 있음

# while right < N:
#     if sum_ >= S:
#         result = min(right - left, result)
#         sum_ -= sequences[left]
#         left += 1
#     else:
#         sum_ += sequences[right]
#         right += 1
# """

# while True:
#     if sum_ >= S:
#         result = min(right - left, result)
#         sum_ -= sequences[left]
#         left += 1
#     elif right == N:
#         break
#     else:
#         sum_ += sequences[right]
#         right += 1

# if result == N+1:
#     print(0)
# else:
#     print(result)

def divsum(N):
    result = 0
    for i in range(1, N):
        ls = list(map(int, str(i))) 
        
        result = i + sum(ls)
        if result == N:
            return i
    return 0

N = int(input())
print(divsum(N))