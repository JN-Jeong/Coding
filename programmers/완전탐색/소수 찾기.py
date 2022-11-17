from itertools import permutations


def is_prime_num(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    prime_num = []
    for i in range(1, len(numbers) + 1):
        arr = list(permutations(numbers, i))
        print(arr)
        for j in range(len(arr)):
            num = int("".join(map(str, arr[j])))
            # print(num)
            if is_prime_num(num):
                prime_num.append(num)
    # print(arr)

    answer = len(list(set(prime_num)))
    return answer


numbers = ["17", "011"]
returns = [3, 2]

for number in numbers:
    print(solution(number))
