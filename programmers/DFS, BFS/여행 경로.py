"""
tickets가
[["ICN", "B"], ["B", "C"], ["C", "ICN"], ["ICN", "D"], ["ICN", "E"], ["E", "F"]]
로 주어졌을 때
정답이
["ICN", "B", "C", "ICN", "E", "F", "D"]
인데
어떻게 F에서 D로 방문할 수 있는 것이지?
"""

from collections import defaultdict


def solution(tickets):
    answer = []

    routes = defaultdict(list)
    for dep, des in tickets:  # 방문할 수 있는 항공권 그래프 생성
        routes[dep].append(des)

    print(routes)

    def dfs():
        q = ["ICN"]
        paths = []

        while len(q) > 0:
            dep = q[-1]  # departure

            print("dep : ", dep)
            print("routes : ", routes)

            if dep not in routes or len(routes[dep]) == 0:
                paths.append(q.pop())   # stacks에서 목적지가 없어짐
            else:
                q.append(routes[dep].pop(0))    # routes에서 목적지가 없어짐

            print("paths : ", paths)
            print("stack : ", q)
            print("routes : ", routes)
        
        print()
        return paths[::-1]

    for r in routes:
        routes[r].sort()  # 알파벳 순으로 정렬
    print(routes)

    answer = dfs()

    return answer


tickets = [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	, [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]],]
returns = [["ICN", "JFK", "HND", "IAD"],["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],]

for ticket in tickets:
    print(solution(ticket))