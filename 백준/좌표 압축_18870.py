N = int(input())
nums = list(map(int, input().split()))

set_X = {}
idx = 0
for i in sorted(nums):
    if i not in set_X:
        set_X[i] = idx
        idx += 1

for n in nums:
    print(set_X[n], end = ' ')