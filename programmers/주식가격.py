# def solution(prices):
#     answer = [0] * len(prices)
    
#     # 각 주식이 가격이 떨어지지 않은 기간이 몇 초인지 list로 반환

#     time = 0
#     price = 0 # 현재 금액
#     while time < len(prices): # 
#         price = prices[time]
#         time += 1
#         print(price, time)
#         for i in range(time):
#             if prices[i] <= price: # 가격이 떨어지지 않았다면
#                 answer[i] += 1
#             else: # 가격이 떨어졌다면
#                 prices[i] = 10001
    
#     print(answer)
#     return answer


from collections import deque


def solution(prices):
    answer = []
    
    # 각 주식의 가격이 떨어지지 않은 기간이 몇 초인지 list로 반환
    
    q = deque(prices)

    while q:
        price = q.popleft()
        time = 0

        for i in q:
            time += 1
            if price > i:
                break
        answer.append(time)
                
    print(answer)
    return answer