# nums = list(input())
# nums.sort(reverse=True)
# print(''.join(nums))


# # 패캠 강의의 접근법
# nums = list(input())
# sorts = [0] * 10    # 0 ~ 9까지 저장할 리스트

# for n in nums:
#     sorts[int(n)] += 1

# for i in range(10-1, -1, -1):   # 0 ~ 9 index에 저장된 값만큼 반복해서 해당 index 숫자를 출력
#     for j in range(sorts[i]):
#         print(i, end='')

# 패캠 강의 풀이
nums = input()
for i in range(10-1, -1, -1):
    for j in nums:
        if int(j) == i:
            print(i, end ='')