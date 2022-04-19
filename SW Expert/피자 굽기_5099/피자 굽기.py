"""
마지막까지 남아있는 피자 번호를 반환
index가 필요

"""

from collections import deque


def solve():
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    for i, p in enumerate(pizzas):
        pizzas[i] = (p, i)

    oven = deque()
    for i in range(N):
        oven.append(pizzas[i])
    print(oven)

    pizzas = deque(pizzas[N:])

    while oven:
        if len(oven) == 1:
            return oven[0][1] + 1

        cheese, i = oven.popleft()

        if cheese == 1: # 치즈가 다 녹았다면 pizzas에서 제외해줌
            if pizzas:
                oven.append(pizzas.popleft())
        else: # 치즈가 다 녹지 않았다면 화덕에 다시 추가
            oven.append((cheese//2, i))
        
        print("oven : ", oven)
        print("pizzas : ", pizzas)

if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print("#{} {}".format(i, solve()))