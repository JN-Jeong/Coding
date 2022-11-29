"""
성능 검사 : 열, 연속 3개
약품 투입 : 행

"""

import copy


# 성능 검사 함수
def is_pass(arr):

    cur = '0' # 현재 특성
    conti = 0 # 연속된 특성 개수
    for col in range(len(arr[0])):
        for row in range(len(arr)):
            if arr[row][col] == cur:
                conti += 1
            elif arr[row][col] != cur:
                cur = arr[row][col]
                conti = 1
        if conti > K:
            break

        if conti < K: # 연속된 특성 개수가 통과 개수보다 낮으면 통과 실패
            # print(arr)
            # print("성능 검사 통과 실패", conti)
            return False
    return True

# 약품 투입 함수
def injection(arr, idx, cnt, N): # idx : 약품 투입 할 행 index, N : A or B 투입
    for i in range(len(arr[0])):
        arr[idx][i] = N

    return arr, cnt+1


def dfs(arr, idx, injected, cnt): # arr : 필름, idx : 약품 투입 행, injected : 약품 투입 상황, cnt : 약품 투입 횟수
    global min_count
    if cnt > K: # 약품 투입 수가 통과 개수보다 많아지면 해당 경우는 탐색 중지
        print("중지 : ", idx)
        # print(arr)
        return arr

    if is_pass(arr): # 성능 검사를 통과하면 필름 반환
        # print(arr)
        if min_count > cnt:
            min_count = cnt
            print("count : ", min_count)
            print(arr)

    injected[idx] = 1
    
    for i in range(len(injected)):
        if injected[i] == 0: # 약품 투입하지 않은 행
            # print(f"idx : {i}")
            # prin1t(arr)

            A_arr, A_cnt = injection(copy.deepcopy(arr), i, cnt, 0) # A 투입
            # print("A")
            # print(A_arr)
            dfs(A_arr, i, copy.deepcopy(injected), A_cnt)
            B_arr, B_cnt = injection(copy.deepcopy(arr), i, cnt, 0) # B 투입
            # print("B")
            # print(B_arr)
            dfs(B_arr, i, copy.deepcopy(injected), B_cnt)
            
            # A_arr, A_cnt = injection(arr, i, cnt, 0) # A 투입
            # dfs(A_arr, i, injected, A_cnt)
            # B_arr, B_cnt = injection(arr, i, cnt, 1) # B 투입
            # dfs(B_arr, i, injected, B_cnt)


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        global K
        D, W, K = map(int, input().split()) # 행 개수, 열 개수, 통과 개수
        global min_count
        min_count = K+1

        films = []
        for _ in range(D):
            films.append(list(map(int, input().split())))
        

        # cells = injection(cells, 2, '0')
        # cells = injection(cells, 5, '1')
        # print(cells)
        
        injected = [0] * D
        print(len(injected))
        for i in range(len(injected)):
            dfs(films, i, injected, 0)