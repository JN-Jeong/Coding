# import sys

# in_f = open('SW Expert/View_1206/input.txt', 'r')
# lines = in_f.readlines()

# # row = int(sys.stdin.readline())
# # columns = list(map(int, sys.stdin.readline().split()))

# for i in range(1, 11):
#     rows = int(input())
#     columns = list(map(int, input().split()))

#     sum_household = 0
#     for j in range(2, len(columns)-2):
#         # left
#         max_left = max(columns[j-1], columns[j-2])
#         l_num_household = columns[j] - max_left

#         # right
#         max_right = max(columns[j+1], columns[j+2])
#         r_num_household = columns[j] - max_right

#         num_household = min(l_num_household, r_num_household)

#         if columns[j] > num_household > 0:
#             sum_household += num_household

#     print("#{} {}".format(i, sum_household))
    
# in_f.close()

# in_f = open('SW Expert/View_1206/input.txt', 'r')
# lines = in_f.readlines()

# # row = int(sys.stdin.readline())
# # columns = list(map(int, sys.stdin.readline().split()))

# for i in range(1, 11):
#     row = int(lines[i])
#     columns = list(map(int, lines[i+1].split()))

#     sum_household = 0
#     for j in range(2, len(columns)-2):
#         num1 = columns[j] - columns[j-1]
#         num2 = columns[j] - columns[j-2]
#         num3 = columns[j] - columns[j+1]
#         num4 = columns[j] - columns[j+2]

#         if num1 > 0 and num2 > 0 and num3 > 0 and num4 > 0:
#             sum_household += min(num1, num2, num3, num4)

#     print("#{} {}".format(i, sum_household))

# in_f.close()

in_f = open('SW Expert/View_1206/input.txt', 'r')
lines = in_f.readlines()

# row = int(sys.stdin.readline())
# columns = list(map(int, sys.stdin.readline().split()))

for i in range(0, 10):
    row = int(lines[i*2])
    columns = list(map(int, lines[i*2+1].split()))

    sum_household = 0
    for j in range(2, len(columns)-2):
        near_household = max(columns[j-1], columns[j-2], columns[j+1], columns[j+2])
        num_household = columns[j] - near_household

        if num_household > 0:
            sum_household += num_household

    print("#{} {}".format(i, sum_household))

in_f.close()
