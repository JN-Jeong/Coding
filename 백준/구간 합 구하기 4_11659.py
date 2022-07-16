'''
5 3
5 4 3 2 1
1 3
2 4
5 5

12
9
1
---------------
'''

import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
print(nums)

temp = [0] * (N+1)
for i in range(1, len(temp)):
    temp[i] += temp[i-1] + nums[i-1]
print(temp)

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(temp[n2] - temp[n1-1])
    