N = int(input())

new_N = N
res = 0
while True:
    res += 1
    if new_N < 10:
        new_N = new_N * 10 + new_N

    else:
        one_digit = new_N % 10
        ten_digit = new_N // 10
        new_one_digit = (one_digit + ten_digit) % 10
        new_N = one_digit * 10 + new_one_digit

    if new_N == N:
        print(res)
        break