"""
1, 2, 3, 2, 5 : 6
4, 3, 2, 1, 3 : 3  -> 3, 1, 2, 3, 4
1, 2, 4, 3, 2, 1, 2, 3 : 6 -> 3, 2, 1, 2, 3, 4, 2, 1

역순으로 max 가격을 갱신하고 max 가격보다 낮은 가격이라면 정산하여 이득보기
"""

def solve():
    N = int(input())
    prices = list(map(int, input().split()))

    profit = 0
    max_ = prices[-1]
    for i in range(N-1, -1, -1):
        if max_ < prices[i]:
            max_ = prices[i]
        
        if max_ > prices[i]:
            profit += max_ - prices[i]

    print(profit)
    return profit


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print(f"#{i} {solve()}")
