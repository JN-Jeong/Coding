n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
print(nums)

result = 0

left, right = 0, n-1
while left < right:
    if nums[left] + nums[right] > x:
        right -= 1
    elif nums[left] + nums[right] < x:
        left += 1
    elif nums[left] + nums[right] == x:
        result += 1
        right -= 1
        left += 1

print(result)