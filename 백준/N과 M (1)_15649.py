# N, M = map(int,(input().split()))

# def permu(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in permu(arr[:i] + arr[i+1:], r-1):
#                 yield [arr[i]] + next

# arr = [i for i in range(1, N+1)]

# for s in list(permu(arr, M)):
#     for n in s:
#         print(n, end = ' ')
#     print()


N, M = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,N+1):
        if i not in s:  # 원소의 중복을 허용하지 않음
            s.append(i)
            dfs()
            s.pop()
 
dfs()