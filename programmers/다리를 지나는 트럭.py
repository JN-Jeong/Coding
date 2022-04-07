# 문제에서 주어진 트럭이 정해진 순으로 건너기 때문에 순서를 변경하여 최소 시간을 구하지 않아도 됨
# 문제를 잘 읽어보자(트럭 순서까지 고려하여 최소 시간을 구하려고 노력했는데..)

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
    
#     # 모든 트럭이 다리를 건너는데 걸리는 최소 시간을 반환
#     # bridge_length = 동시에 다리에 올라갈 수 있는 트럭 수
#     # weight = 다리가 버틸 수 있는 무게
    
#     time = 0
#     num_truck = len(truck_weights) # 트럭 수
#     cross_trucks = [] # 다리 위의 트럭
#     crossed_trucks = [] # 다리를 지난 트럭
#     sum_weight = 0 # 다리 위의 트럭 무게
#     while len(crossed_trucks) < num_truck:
#         time += 1        
        
#         if len(cross_trucks) > 0 and (time - cross_trucks[0][1]) == bridge_length:
#             crossed_trucks.append(cross_trucks.pop(0)) # 다리를 지난 트럭 추가
#             sum_weight -= crossed_trucks[-1][0] # 다리를 지난 트럭 무게 빼줌
        
#         for i in range(len(truck_weights)):
#             if (sum_weight + truck_weights[i]) <= weight: # 다리 위의 트럭 무게와 건널 트럭 무게가 
#                                                          # weight보다 작다면
#                 cross_trucks.append((truck_weights.pop(i), time)) # 다리 위의 트럭과 현재 시간 추가
#                 sum_weight += cross_trucks[0][0] # 다리 위의 트럭 무게 더해줌
#                 break
        
#         # print("시간 : ", time)
#         # print("다리 위 트럭 : ", cross_trucks)        
#         # print("남은 트럭 : ", truck_weights)
        
#     print(time)
#     answer = time
    
#     return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 모든 트럭이 다리를 건너는데 걸리는 최소 시간을 반환
    # bridge_length = 동시에 다리에 올라갈 수 있는 트럭 수 (int)
    # weight = 다리가 버틸 수 있는 무게 (int)
    
    time = 0
    cross_trucks = [0] * bridge_length # 다리 위의 트럭
    sum_weight = 0 # 다리 위의 트럭들 무게
    while len(cross_trucks):
        time += 1
        sum_weight -= cross_trucks.pop(0)
        
        if truck_weights:
            if sum_weight + truck_weights[0] <= weight:
                cross_trucks.append(truck_weights.pop(0))
                sum_weight += cross_trucks[-1]
            else:
                cross_trucks.append(0)
        # print(cross_trucks)
    answer = time
    
    return answer