def solution(n, k):
    answer = 0

    temp = ""
    while n > 0:
        temp += str(n % k)
        n //= k

    print(temp[::-1].split("0"))
    for num in temp[::-1].split("0"):
        if num:
            if is_prime(int(num)) > 0:
                answer += 1
    return answer


# def is_prime(n):
#     nums = [0] * (n + 1)
#     for i in range(2, n + 1):
#         nums[i] = i

#     for i in range(2, int(n**0.5) + 1):
#         if nums[i] == 0:
#             continue
#         for j in range(i**2, n + 1, i):
#             nums[j] = 0

#     return nums[-1]


def is_prime(n):
    if n == 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0

    return n


if __name__ == "__main__":
    ns = [437674, 110011]
    ks = [3, 10]
    result = [3, 2]
    for n, k in zip(ns, ks):
        print(solution(n, k))
