X = int(input())

cal_dict = {}
num_2 = 2
num_3 = 3

num = 1
while num_2 < 10**6 and num_3 < 10**6:
    num_2 = num_2 * num
    num_3 = num_3 * num

    if num_2 > 10**6:
        break
    if num_3 > 10**6:
        break

    if not num_2 in cal_dict:
        cal_dict[num_2] = num
    if not num_3 in cal_dict:
        cal_dict[num_3] = num
    
    num += 1

count = 0
while X > 1:
    if X in cal_dict:
        print(cal_dict[X] + count)
        break
    
    X -= 1
    count += 1