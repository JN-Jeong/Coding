# """
# python3는 시간초과
# pypy3는 통과
# """

# X = int(input())

# i, j = 0, 0
# flag = True

# d = [[0, 1], [1, 0], [1, -1], [-1, 1]]
# for _ in range(X-1):
#     if i == 0 and j == 0:
#         i += d[0][0]
#         j += d[0][1]
    
#     elif j % 2 == 1 and i == 0:
#         i += d[2][0]
#         j += d[2][1]

#     elif i % 2 == 1 and j == 0:
#         i += d[1][0]
#         j += d[1][1]

#     elif i % 2 == 0 and j == 0:
#         flag = True     # 대각선 위로 d[3]
#         i += d[3][0]
#         j += d[3][1]
    
#     elif j % 2 == 0 and i == 0:
#         flag = False    # 대각선 아래로 d[2]
#         i += d[0][0]
#         j += d[0][1]

#     elif flag:
#         i += d[3][0]
#         j += d[3][1]

#     elif not flag:
#         i += d[2][0]
#         j += d[2][1]

# print(f"{i+1}/{j+1}")


"""
규칙을 통해 구현
패캠 강의 풀이
"""

X = int(input())
line = 0            # X가 존재하는 대각선이 몇 번째 대각선인지 구함
max_num = 0         # X가 존재하는 대각선에서 가장 큰 숫자
while X > max_num:
    line += 1
    max_num += line

gap = max_num - X

# 대각선이 짝수 번째일 때
if line % 2 == 0:       
    top = line - gap    # 분자
    under = gap + 1     # 분모

# 대각선이 홀수 번째일 때
else:                   
    top = gap + 1       # 분자
    under = line - gap  # 분모

print(f"{top}/{under}")