"""
프로그래머스 : 금과 은 운반하기
"""


def solution(a, b, g, s, w, t):
    # 최악의 경우
    # 걸리는 최소시간(왕복) : 2
    # 금 따로 은 따로(한도시에 금,은만 있을경우) : 2
    # 광물의 최대무게 : 10**9
    # 도시의 최대개수 : 10**5
    start = 0
    end = (10**9) * 2 * (10**5) * 2

    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]

            move_cnt = mid // (now_time * 2)

            if mid % (now_time * 2) >= now_time:
                move_cnt += 1

            gold += min(now_gold, move_cnt * now_weight)
            silver += min(now_silver, move_cnt * now_weight)
            total += min(now_gold + now_silver, move_cnt * now_weight)

        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
        else:
            start = mid + 1

    answer = start
    return answer


if __name__ == "__main__":
    need_golds = [10, 90]
    need_silvers = [10, 500]
    golds = [[100], [70, 70, 0]]
    silvers = [[100], [0, 0, 500]]
    weights = [[7], [100, 100, 2]]
    times = [[10], [4, 8, 1]]
    result = [50, 499]

    for i, data in enumerate(zip(need_golds, need_silvers, golds, silvers, weights, times)):
        a, b, g, s, w, t = data
        print(f"#{i}", solution(a, b, g, s, w, t))
