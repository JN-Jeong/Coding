# import sys

# N = int(sys.stdin.readline())

# nums = {}
# for i in range(N):
#     num = int(input())
#     if num not in nums:
#         nums[num] = 0
#     nums[num] += 1

# for i in range(1, 10000):
#     if i not in nums:
#         continue
#     for j in range(nums[i]):
#         print(i)


import sys

a = int(sys.stdin.readline())
num_set = {}
for i in range(a):
    num = int(sys.stdin.readline())
    if num not in num_set:
        num_set[num] = 0
    num_set[num] += 1

for i, j in sorted(num_set.items()):
    for k in range(j):
        print(i)