from collections import deque


def solution(tickets):
        
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            answer = []
            q = deque()
            q.append(tickets[i])
            visited = [0] * len(tickets)
        else:
            continue
            
        while q:
            dep, des = q.popleft()

            for i in range(len(tickets)):
                if visited[i] == 0 and tickets[i][0] == des:
                    visited[i] = 1
                    q.append(tickets[i])
                    print(q)
                    answer.append(des)
        answer.append(des)
        print(answer)
    # answer.append(des)
    # print(answer)
    return answer