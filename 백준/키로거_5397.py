# # 런타임 에러 발생
# # if문이 너무 많아지고 복잡함
# if __name__ == '__main__':
#     T = int(input())

#     for _ in range(T):
#         keylogger = input()
#         password = []
#         i = -1
#         for key in keylogger:
#             if key == "<":
#                 if i > -1:
#                     i -= 1
#                 else:
#                     i = -1
#             elif key == ">":
#                 if i >= len(password):
#                     pass
#                 else:
#                     i += 1
#             elif key == "-":
#                 if password and i > -1:
#                     print(password, i)
#                     password.pop(i)
#             else:
#                 password.insert(i+1, key)
#                 i += 1

#         print(''.join(password))



"""
패캠 강의 풀의

스택을 왼쪽, 오른쪽으로 두 개 만듬
스택 두 개의 중간 지점을 커서로 간주
문자 입력 : 왼쪽 스택에 원소 삽입
- 입력 : 왼쪽 스택의 원소 삭제
< 입력 : 왼쪽 스택의 원소를 삭제하고 오른쪽 스택에 왼쪽 스택에서 삭제한 원소 추가
> 입력 : 오른쪽 스택의 원소를 삭제하고 왼쪽 스택에 오른쪽 스택에서 삭제한 원소 추가

오른쪽 스택에는 역방향으로 문자가 추가되어 있기 때문에
출력 시 오른쪽 스택을 반대로(reversed) 출력해줌
"""

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        lstack = []
        rstack = []
        keylogger = input()
        for key in keylogger:
            if key == '<':
                if lstack:
                    rstack.append(lstack.pop())
            elif key == '>':
                if rstack:
                    lstack.append(rstack.pop())
            elif key == '-':
                if lstack:
                    lstack.pop()
            else:
                lstack.append(key)

        # print(''.join(lstack) + ''.join(reversed(rstack)))
        lstack.extend(reversed(rstack))
        print(''.join(lstack))