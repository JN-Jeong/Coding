# T = int(input())

# for i in range(1, T+1):
#     K, N, M = map(int, input().split())
#     stop = list(map(int, input().split()))

#     flag = True
#     num = N//K
#     for j in range(len(stop)-1, 0, -1):
#         if N - stop[-1] > K:
#             flag = False
#             break

#         if stop[0] > K:
#             flag = False
#             break

#         if stop[j] - stop[j-1] > K:
#             flag = False
#             break

#     if flag:
#         print('#{} {}'.format(i, num))
#     else:
#         print('#{} {}'.format(i, 0))


T = int(input())

for i in range(1, T+1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split())) # 충전 정류장 번호
    charge_num = 0 # 충전횟수
    stop = 0 # 현재 정류장 번호
    
    # 마지막 정류장에 도달할 때까지 반복
    while stop + K < N:
        # 한번 충전으로 이동할 수 있는 횟수만큼 반복
        for step in range(K, 0, -1):
            # 충전이 가능한 정류장까지 갈 수 있다면
            if stop + step in charges:
                stop += step # 현재 위치 갱신
                charge_num += 1 # 충전 횟수 증가
                break
        
        else:
            charge_num = 0
            break
        
    print('#{} {}'.format(i, charge_num))
