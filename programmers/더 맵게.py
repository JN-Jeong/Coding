import heapq

def solution(scoville, K):
    answer = 0
    
    # 모든 음식을 섞어야 하는 최소 횟수를 반환 (int)
    
    heapq.heapify(scoville)
    # print(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2*2)
        answer += 1
        # print(scoville)
        
    return answer