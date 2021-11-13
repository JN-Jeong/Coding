N = int(input())

def facto(num):
    if num < 2:
        return num
    
    return num * facto(num-1)

def zero_num(num):
    res = 0
    str_num = str(num)
    for i in range(1, len(str_num)):
        if str_num[-i] == '0':
            res += 1
        else:
            return res
    return res

N_facto = facto(N)
print(zero_num(N_facto))