'''
1 2 3 4 5 6 7 8 9 10
3 5 7 -10 1 9 8 7 6
10 -1 10 -5 100
10 -11 10 -11 100
'''
n = int(input())
seq = list(map(int, input().split()))

temp = 0
res = -1001
for i in range(n):
    temp += seq[i]
    if temp <= 0:
        res = max(res,temp)
        temp = 0
    else:
        res = max(res,temp)
    
print(res)