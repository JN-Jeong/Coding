"""
kruskal 알고리즘
"""

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    print(costs)
    
    connect = [costs[0][0]]
    
    while len(connect) != n:
        for i, cost in enumerate(costs):
            if cost[0] in connect and cost[1] in connect:
                continue

            if cost[0] in connect or cost[1] in connect:
                connect.append(cost[0])
                connect.append(cost[1])
                answer += cost[2]

                connect = list(set(connect))
                print(connect)
                print(answer)
                break
        
    return answer