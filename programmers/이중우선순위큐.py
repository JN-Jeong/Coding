import heapq

def solution(operations):
    answer = []
    q = []
    
    for i in range(len(operations)):
        oper, num = operations[i].split(" ")
        num = int(num)
        # print(oper, num) 
        if oper == "I":
            heapq.heappush(q, num)
        if oper == "D":
            if len(q) > 0:
                if num == 1: # 최댓값 삭제
                    q = heapq.nlargest(len(q), q)[1:] # 최댓값을 제외하고 heap 반환
                    heapq.heapify(q)
                elif num == -1: # 최솟값 삭제
                    heapq.heappop(q)
        
        # print(q)

    if q: # 큐가 비어있지 않다면
        answer.append(max(q))
        answer.append(min(q))
    else: # 큐가 비어있다면
        answer = [0,0]
        
    return answer