def solution(cards):
    answer = 1
    cards = [0] + cards

    visited = [0] * len(cards)
    boxes = []
    for i in range(1, len(cards)):
        if visited[i]:
            continue

        visited[i] = 1  # 현재 index 방문 기록
        n = 1
        card = cards[i]
        while not visited[card]:
            visited[card] = 1
            card = cards[card]
            n += 1

        print(n)
        print(visited)
        boxes.append(n)

    boxes.sort()
    if len(boxes) == 1:
        return 0

    answer = boxes[-1] * boxes[-2]
    return answer


cards = [[8, 6, 3, 7, 2, 5, 1, 4], [1, 6, 3, 7, 2, 5, 8, 4]]
results = [12]

for card in cards:
    print(solution(card))
    print()
