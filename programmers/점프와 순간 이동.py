"""
Summer/Winter Coding(~2018)
점프와 순간 이동

n부터 2로 나누면서 답을 구한다.
2로 나눠지지 않으면 순간 이동이 불가능하고 점프가 필요하기 때문에 건전지(answer) + 1

4 = 0b100
8 = 0b1000
2의 n제곱이면 처음 0에서 1로 점프하는 순간 빼고 순간이동으로 이동 가능
(2의 제곱수들을 이진수로 표현하면 1이 하나)
건전지 사용량은 이진수로 변환했을 때 1의 개수와 같음
"""


# def solution(n):
#     answer = 0

#     while n > 0:
#         answer += n % 2
#         n //= 2
#     return answer


def solution(n):
    answer = 0
    binn = bin(n)
    answer = binn.count("1")
    return answer


if __name__ == "__main__":
    ns = [5, 6, 5000, 200000000]
    results = [2, 2, 5]

    for i, data in enumerate(ns):
        n = data
        print(f"#{i}", solution(n))
