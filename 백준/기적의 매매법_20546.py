def solution():
    cash = int(input())
    prices = list(map(int, input().split()))
    JH = {"cash": cash, "price": 0, "num": 0}
    SM = {"cash": cash, "price": 0, "num": 0}

    flag = [0, 0]  # 0: 가격 상승, 1: 가격 하락

    for i in range(len(prices) - 1):
        if flag[0] >= 3:  # 3일 연속 가격 상승 => 가격 하락, 전량 매도
            SM["cash"] += prices[i] * SM["num"]
            SM["num"] = 0
        elif flag[1] >= 3:  # 3일 연속 가격 하락 => 가격 상승, 전량 매수
            num = SM["cash"] // prices[i]
            SM["cash"] -= num * prices[i]
            SM["num"] += num

        if prices[i] <= JH["cash"]:
            num = JH["cash"] // prices[i]
            JH["cash"] -= num * prices[i]
            JH["price"] = prices[i]
            JH["num"] += num

        if prices[i] < prices[i + 1]:
            flag[0] += 1
            flag[1] = 0
        elif prices[i] > prices[i + 1]:
            flag[0] = 0
            flag[1] += 1
        else:
            flag[0] = 0
            flag[1] = 0

        # print(SM)
    # print(JH)
    # print(SM)

    if JH["num"] * prices[-1] + JH["cash"] > SM["num"] * prices[-1] + SM["cash"]:
        print("BNP")
    elif JH["num"] * prices[-1] + JH["cash"] < SM["num"] * prices[-1] + SM["cash"]:
        print("TIMING")
    else:
        print("SAMESAME")


if __name__ == "__main__":
    solution()
