def solution(tickets):
    answer = []
    for i in range(len(tickets)):
        visited = [0] * len(tickets)
        visited[i] = 1
        if tickets[i][0] == "ICN":
            paths = [tickets[i][0]]
        else:
            continue
        dfs(visited, i, paths, tickets)
        answer.append(paths)
    
    answer.sort()
    answer = answer[0]
    return answer


def dfs(visited, idx, paths, tickets):
    if len(visited) == sum(visited):
        return
    
    for i in range(len(tickets)):
        if visited[i] == 0 and tickets[idx][1] == tickets[i][0]:
            visited[i] = 1
            print(visited)
            if len(visited) == sum(visited): # 마지막 방문
                paths.append(tickets[i][0])
                paths.append(tickets[i][1])
            else:
                paths.append(tickets[i][0])
            print(paths)
            dfs(visited, i, paths, tickets)