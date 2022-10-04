def solution(X, receipt):
    total = 0

    for price, num in receipt:
        total += price * num
    
    if X == total:
        return 'Yes'
    return 'No'

if __name__ == "__main__":
    X = int(input())
    N = int(input())
    receipt = []
    for _ in range(N):
        receipt.append(list(map(int, (input().split()))))

    print(solution(X, receipt))