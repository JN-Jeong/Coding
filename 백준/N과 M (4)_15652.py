# N, M = map(int, input().split())

# def permu(start):
#     if len(seq) == M:
#         print(' '.join(map(str, seq)))
#         return
#     else:
#         for i in range(start, N + 1):
#             seq.append(i)
#             permu(i)
#             seq.pop()

# seq = []
# permu(1)


N, M = list(map(int,input().split()))
 
s = []
 
def dfs(start):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, N+1):
        s.append(i)
        dfs(i)      # 조합의 중복을 허용하지 않음
        s.pop()
 
dfs(1)