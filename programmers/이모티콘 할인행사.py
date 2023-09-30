"""
이모티콘별로 할인율이 매겨진다
"""
from itertools import product


def solution(users, emoticons):
    answer = [0, 0]  # 서비스 가입, 결제금액

    sales = [10, 20, 30, 40]

    for sale in list(product(sales, repeat=len(emoticons))):
        user_buy = [[0, 0] for _ in range(len(users))]
        for i in range(len(users)):
            service = 0
            buy = 0
            for j in range(len(emoticons)):
                if users[i][0] <= sale[j]:  # 특정 할인 이상 하면 구매
                    buy += emoticons[j] * (1 - sale[j] * 0.01)

            if buy >= users[i][1]:  # 서비스 가입
                service += 1
                buy = 0

            user_buy[i] = [service, buy]

        # print(sale)
        # print(user_buy)
        # print()

        n_service = 0
        price = 0
        for u_b in user_buy:
            n_service += u_b[0]
            price += u_b[1]
        # print(n_service, price)

        if answer[0] < n_service:
            answer[0] = n_service
            answer[1] = 0
        if answer[0] == n_service:
            answer[1] = max(answer[1], price)

    return answer


users = [[[40, 10000], [25, 10000]], [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]]
emoticons = [[7000, 9000], [1300, 1500, 1600, 4900]]

result = [[1, 5400], [4, 13860]]

for user, emoticon in zip(users, emoticons):
    print(solution(user, emoticon))
