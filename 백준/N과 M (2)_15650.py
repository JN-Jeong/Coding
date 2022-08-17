# N, M = map(int, input().split())

# def permu(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in permu(arr[:i] + arr[i+1:], r - 1):
#                 yield [arr[i]] + next

# arr = [i for i in range(1, N+1)]

# seq = permu(arr, M)
# # print(list(seq))
# dup = []
# for s in list(seq):
#     if sorted(s) not in dup:
#         for n in s:
#             print(n, end = ' ')
#         print()
#         dup.append(s)
#     print(dup)


N, M = list(map(int,input().split()))
 
s = []
 
def dfs(start):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, N+1):
        if i not in s:      # 원소의 중복을 허용하지 않음
            s.append(i)
            dfs(i + 1)
            s.pop()
 
dfs(1)