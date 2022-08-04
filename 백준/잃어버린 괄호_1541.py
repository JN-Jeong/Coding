# equation = input()

# nums = []
# opers = []
# num = ''
# for e in equation:
#     if e == '-':
#         nums.append(int(num))
#         num = ''
#         opers.append(e)
#     elif e == '+':
#         nums.append(int(num))
#         num = ''
#         opers.append(e)
#     else:
#         num += e
# nums.append(int(num))

# answer = nums[0]
# flag = False
# for oper, num in zip(opers, nums[1:]):
#     if oper == '-':
#         flag = True
    
#     if flag:
#         answer -= num
#     else:
#         answer += num

# print(answer)


equation = input().split('-') # -를 기준으로 식을 분리

result = 0
for i in equation[0].split('+'): # - 가 나오기 전 숫자들은 모두 더해줌
    result += int(i)

for i in equation[1:]: # 첫 번째 - 가 나온 이후의 숫자들은 모두 괄호를 통해 음수가 될 수 있음
    for j in i.split('+'): # +를 기준으로 숫자들을 분리
        result -= int(j)

print(result)