N = int(input())

trophys = []
for _ in (range(N)):
    trophys.append(int(input()))
    
left = 0        # 왼쪽에서 봤을 때 보이는 트로피 수
right = 0       # 오른쪽에서 봤을 때 보이는 트로피 수
l_temp = 0      # 왼쪽에서 봤을 때 이전 트로피의 높이
r_temp = 0      # 오른쪽에서 봤을 때 이전 트로피의 높이
for l, r in enumerate(range(N-1, -1, -1)):
    if l_temp < trophys[l]:
        l_temp = trophys[l]
        left += 1

    if r_temp < trophys[r]:
        r_temp = trophys[r]
        right += 1

print(left)
print(right)


# # 패캠 강의 풀이
# def ascending(array):
#     now = array[0]
#     result = 1
#     for i in range(1, len(array)):
#         if now < array[i]:
#             result += 1
#             now = array[i]
#     return result

# n = int(input())
# array = []

# for _ in range(N):
#     array.append(int(input()))

# print(ascending(array))
# array.reverse()
# print(ascending(array))