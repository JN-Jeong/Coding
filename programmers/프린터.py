# def solution(priorities, location):
#     answer = 0

#     # location의 값이 몇번째로 출력되는지 반환
#     # priorities의 값은 중요도, 값이 높을수록 중요하다는 뜻
#     # 첫번째로 인쇄는 1 반환, 두번째는 2반환
    
#     print(priorities)
    
#     num = 0
#     while len(priorities) > 0:
#         if location == 0:
#             if priorities[0] < max(priorities):
#                 priorities.append(priorities.pop(0))
#                 location = len(priorities) - 1
#             else:
#                 return num + 1
#         else:
#             if priorities[0] < max(priorities):
#                 priorities.append(priorities.pop(0))
#                 location -= 1
#             else:
#                 priorities.pop(0)
#                 location -= 1
#                 num += 1
    
#     print(num)
#     answer = num
    
#     return answer


def solution(priorities, location):
    answer = 0

    # location의 값이 몇번째로 출력되는지 반환
    # priorities의 값은 중요도, 값이 높을수록 중요하다는 뜻
    # 첫번째로 인쇄는 1 반환, 두번째는 2반환
    
    search = sorted(priorities, reverse=True)
    count = 0

    while count < len(priorities):
        for i, priority in enumerate(priorities):
            s = search[count]
            if priority == s:
                count += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break

    return answer