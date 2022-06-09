# import sys
# a = int(sys.stdin.readline())

# stack_list = []
# print_list = []
# count = 0
# com = True
# for i in range(1, a+1):
#     stack_list.append(i)
#     print_list.append('+')
#     while True:
#         if count == a+1:
#             break
#         if len(stack_list) == 0:
#             break
#         if com:
#             num = int(sys.stdin.readline())
#             com = not com
#         if num == stack_list[-1]:
#             print_list.append('-')
#             stack_list.pop()
#             com = not com
#             count += 1
#         else:
#             break

# if a == count:
#     for i in print_list:
#         print(i)
# else:
#     print('NO')

if __name__ == "__main__":
    n = int(input())

    count = 1
    stack = []
    result = []
    for _ in range(n):
        num = int(input())
        while count <= num:
            stack.append(count)
            count += 1
            result.append('+')
        
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            exit(0)

    print('\n'.join(result))