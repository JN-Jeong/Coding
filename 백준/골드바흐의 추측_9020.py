def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


T = int(input())

for _ in range(T):
    n = int(input())

    for i in range(
        n // 2, n
    ):  # 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력해야 하기 때문에 n // 2부터 탐색
        if is_prime(i):
            if is_prime(n - i):
                print(n - i, i)
                break
