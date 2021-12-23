# # min_ = len(A) + 1 # 만족할 수 있는 최소 연속 개수
# # for i in range(len(A)):
# #     sum_ = A[i]
# #     for j in range(i+1, len(A)):
# #         sum_ += A[j]
# #         if sum_ > S:
# #             if min_ > j - i:
# #                 min_ = j - i

# # print(min_ + 1)


# # candle = {}
# # num_list = []
# # for i in A:
# #     while i > 0:
# #         num = i % 10
# #         i = i // 10
# #         num_list.append(i)

# # for i in num_list:
# #     # if not i in candle:
# #     #     if i == 9 or i == 6:
# #     #         candle[6] = 0
# #     #     else:
# #     #         candle[i] = 0
# #     # if i == 9 or i == 6:
# #     #     candle[6] += 1
# #     # else:
# #     #     candle[i] += 1

# #     if not i in candle:
# #         candle[i] = 0
# #     candle[i] += 1

# # {1:1, 2:3, 3:2, 4:---, 6:3, ---}

# # max_ = 0
# # for key, value in candle:
# #     if key == 6:
# #         value = int((value+1)/2)

# #     if max_ < value:
# #         max_ = value

# # answer = max_



# # 2x^4 + ----
# # split(' + ')

# # b = sorted(a, key = lambda x:-x[3])
# # 3x^3 + 3x^3 = 6x^3

# # b.split('x^')
# # [2, 6]
# # [3, 5]
# # c = [[2,6], [3,5], [3,6], [4,5], [2,3]]
# # print("입력  : ", c)

# # d = {}
# # for key, value in c:
# #     if not value in d:
# #         d[value] = 0
# #     d[value] += key

# # print(d)

# # num_list = []
# # for value, key in d.items():
# #     num_list.append([key, value])

# # print(num_list)
# # answer = ''
# # for i in range(len(num_list)):
# #     if i == len(num_list) - 1:
# #         answer += str(num_list[i][0]) + 'x^' + str(num_list[i][1])
# #     else:
# #         answer += str(num_list[i][0]) + 'x^' + str(num_list[i][1]) + ' + '

# # print(answer)

# from itertools import permutations

# print(list(permutations([1,2,3,4,5])))


# def DFS(n):
#     visited[n] = True
#     for i in net[n]:
#         if visited[i] == False:
#             DFS[i]

# def DFS(n, computers, com, visited):
#     visited[n] = True
#     for i in range(n):
#         if i != com and computers[com][i] == 1:
#             if visited[i] == False:
#                 DFS(n, computers, i, visited)



# def DFS(n, computer, com, visited):
#     visited[n] = True
#     for i in range(n):
#         if i != com and computer[i][com] == 1:
#             if visited[com] == False:
#                 DFS(n, computer, i, visited)


# def DFS(n, computer, com, visited):
#     visited[n] = True
#     for i in range(n):
#         if i != com and computer[i][com] == 1:
#             if visited[i] == False:
#                 DFS(n, computer, i, visited)


# from collections import deque

# # que = deque()

# # length = len(numbers)
# # que.append([+numbers[0], 0])
# # que.append([-numbers[0], 0])

# # while que:
# #     num, i = que.popleft()

# #     if i+1 == length:
# #         if num == target:
# #             answer += 1
# #     else:
# #         que.append([num + numbers[i+1], i+1])
# #         que.append([num - numbers[i+1], i+1])

# # return answer


# def BFS(n, computers, com, visited):
#     visited[com] = True
#     que = deque()
#     que.append(com)

#     while que:
#         com = que.popleft()
#         for i in range(n):
#             if i != com and computers[com][i] == 1 and visited[i] == False:
#                 visited[i] = True
#                 que.append(i)


# def BFS(n, computers, com, visited):
#     visited[com] = True
#     que = deque()
#     que.append(com)

#     while que:
#         com = que.popleft()
#         for i in range(n):
#             if i != com and computers[com][i] == 1 and visited[i] == False:
#                 visited[i] == True
#                 que.append(i)

# def BFS(n, computers, com, visited):
#     visited[com] = True
#     que = deque()
#     que.append(com)

#     while que:
#         com = que.popleft()
#         for i in range(n):
#             if i != com and computers[com][i] == 1 and visited[i] == False:
#                 visited[i] == True
#                 que.append(i)


# def BFS(numbers, target):
#     length = len(numbers)
#     que = deque()
#     que.append([+numbers[0], 0])
#     que.append([-numbers[0], 0])

#     while que:
#         num, idx = que.popleft()

#         if idx + 1 == length:
#             if num == target:
#                 answer += 1
#         else:
#             que.append([+numbers[idx+1], idx+1])
#             que.append([-numbers[idx+1], idx+1])


# def BFS(n, computers, com, visited):
#     visited[com] = True
#     que = deque()
#     que.append(com)

#     while que:
#         com = que.popleft()
#         for i in range(n):
#             if i != com and computers[com][i] == 1 and visited[i] == False:
#                 visited[i] = True
#                 que.append(i)


# from collections import deque
# from collections import Counter
# from itertools import permutations

# from collections import deque

# def solution(n, computers):
#     answer = 0
#     clen = len(computers)
#     visited = [0] * (clen+1)
    
#     for i in range(n):
#         if visited[i] == 0:
#             bfs(n, computers, i, visited)
#             answer+=1
    
#     return answer

# def bfs(n, computers, i, visited):
#     visited[i] = 1
#     que = deque()
#     que.append(i)
    
#     while que:
#         com = que.popleft()
#         for connect in range(n):
#             if com != connect and computers[com][connect] == 1 and visited[connect] == 0:
#                     visited[connect] = 1
#                     que.append(connect)

# a = []
# print(max(a))

# def BFS(n, computers, com, visited):
#     visited[com] = True
#     que = deque()
#     que.append(com)

#     while que:
#         com = que.popleft()
#         for i in range(n):
#             if i != com and computers[com][i] == 1 and visited[i] == False:
#                 visited[i] = True
#                 que.append(i)


from typing import Coroutine


beg = [2,2,5]
end = [1,4,3]

# [[1,1,0,0,0], [1,1,0,1,0]...]

connect =[]
n=5
for i in range(n+1):
    temp = []
    for j in range(n+1):
        temp.append(0)
    connect.append(temp)

print(connect)

for b, e in zip(beg, end, a):
    connect[b-1][e-1] = connect[e-1][b-1] = 1

print(connect)

from collections import deque

answer = -1

for i in range(n):
    if visited[i] == False:
        BFS(n, connect, i, visited)
        answer += 1

def BFS(n, computer, com, visited):
    visited[com] = True
    que = deque()
    que.append(com)

    while que:
        com = que.popleft()
        for i in range(n):
            if i != com and computer[com][i] == 1 and visited[i] == False:
                visited[i] = True
                que.append(i)
