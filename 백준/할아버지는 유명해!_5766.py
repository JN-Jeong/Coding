def solution():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        players = [list(map(int, input().split())) for _ in range(N)]
        rank = {}
        for player in players:
            for p in player:
                if p not in rank:
                    rank[p] = 0
                rank[p] += 1
        print(rank)

        score = sorted(set(rank.values()))[-2]
        answer = []
        for k, v in rank.items():
            if v == score:
                answer.append(k)

        print(*(sorted(answer)))


if __name__ == "__main__":
    solution()
