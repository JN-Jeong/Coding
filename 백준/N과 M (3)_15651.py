# N, M = map(int, input().split())

# def permu(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in permu(arr[:i] + arr[i:], r-1):
#                 yield [arr[i]] + next

# arr = [i for i in range(1, N+1)]

# seq = permu(arr, M)
# # print(list(seq))
# for s in list(seq):
#     print(' '.join(map(str, s)))

N, M = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()
 
dfs()