n, m = map(int, input().split())

def count_num(n, k):
    count = 0
    while n > 0:
        n //= k
        count += n
    
    return count

count_2 = count_num(n, 2) - count_num(m, 2) - count_num(n-m, 2)
count_5 = count_num(n, 5) - count_num(m, 5) - count_num(n-m, 5)

print(min(count_2, count_5))