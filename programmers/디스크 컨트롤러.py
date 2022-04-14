import heapq

# 각 작업의 요청부터 종료까지 걸린 시간의 평균 반환 (int)

def solution(jobs):
    answer = 0
    idx = 0
    start, now = -1, 0 # 작업 시작 시간, 현재 시간
    heap = []
    
    while len(jobs) > idx:
        # 요청이 들어온 작업들을 소요시간이 적은 순으로 정렬
        
        for job in jobs:
            if start < job[0] <= now: # 요청이 들어온 시점 확인
                heapq.heappush(heap, [job[1], job[0]]) # 작업의 소요 시간을 앞에 두도록 heapq에 추가하여 작업의 소요 시간을 기준으로 정렬 되도록 함
        
        if len(heap) > 0: # 현재 진행될 작업이 존재한다면
            current = heapq.heappop(heap) # 작업을 하나 꺼냄, ex) current == [3, 0]
            start = now # 시작 시간을 현재 시간으로 바꿈
            now += current[0] # 현재 시간에 작업 소요 시간을 더해줌 ex) current[0] == 3(작업 소요 시간)
            answer += (now - current[1]) # 걸린 시간 계산, ex) current[1] == 0(작업 요청 시간)
            idx += 1
        else: # 현재 진행될 작업이 존재하지 않는다면
            now += 1 # 현재 시간을 흐르게 함
        
    answer = answer // len(jobs)
    return answer


# point
# 작업 시작 시간과 현재 시간을 통해 요청이 들어온 시점 확인
# 작업의 소요 시간을 앞에 두도록 heapq에 추가하여 작업의 소요 시간을 기준으로 정렬 되도록 함