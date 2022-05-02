if __name__ == "__main__":
    N, M = map(int, input().split())

    cards = list(map(int, input().split()))

    def blackjack(cards):
        s = 0
        for i in range(len(cards)-2):
            for j in range(i+1, len(cards)-1):
                for k in range(j+1, len(cards)):
                    temp = cards[i] + cards[j] + cards[k]
                    if temp > M:
                        continue
                    elif temp == M:
                        return temp
                    elif s < temp:
                        s = temp

        return s
    
    print(blackjack(cards))
                