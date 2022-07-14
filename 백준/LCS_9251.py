"""
ACAYKP
CAPCAK
4

--------

ABCDEF
EFBCDA
3

--------

ABCDEG
EFBCDA
3

"""

# str1 = input()
# str2 = input()

# memo = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

# for i in range(1, len(str1) + 1):
#     for j in range(1, len(str2) + 1):
#         if str1[i-1] == str2[j-1]:
#             memo[i][j] = memo[i-1][j-1] + 1                     # 알파벳이 같다면 해당 알파벳을 추가하기 전의 값에 + 1 하여 갱신
#         else:
#             memo[i][j] = max(memo[i][j-1], memo[i-1][j])        # 알파벳이 다르다면 이전까지 비교한 값 중 최대값으로 갱신

# print(memo[-1][-1])


str1 = input()
str2 = input()

memo = [0] * len(str2)

for i in range(len(str1)):
    cnt = 0     # 누적 변수
    for j in range(len(str2)):      # memo 순회
        if cnt < memo[j]:           # 현재 누적 변수 값이 memo에 저장된 값보다 작다면 갱신
            cnt = memo[j]
        elif str1[i] == str2[j]:    # 같은 알파벳일 경우 현재 누적 변수에 + 1 하여 해당 알파벳 위치의 memo에 갱신
            memo[j] = cnt + 1
    
    print(cnt, memo)

print(max(memo))