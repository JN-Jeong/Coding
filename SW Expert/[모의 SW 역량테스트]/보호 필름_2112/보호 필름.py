"""
성능 검사 : 열, 연속 3개
약품 투입 : 행

"""

import copy


# 성능 검사 함수
def is_pass(arr, cnt):
    for col in range(W):
        conti = 1 # 연속된 특성 개수
        for row in range(1, D):
            if conti >= K:
                break
            elif arr[row-1][col] == arr[row][col]:
                conti += 1
            else:
                conti = 1

        if conti != K: # 연속된 특성 개수가 통과 개수보다 낮으면 통과 실패
            # print(arr)
            # print("성능 검사 통과 실패", conti)
            return False
    # print("통과", cnt)
    print(arr)
    return True

# 약품 투입 함수
def injection(arr, idx, N): # idx : 약품 투입 할 행 index, N : A or B 투입
    for i in range(W):
        arr[idx][i] = N


def dfs(arr, idx, cnt): # arr : 필름, idx : 약품 투입 행, cnt : 약품 투입 횟수
    global min_count
    if cnt > min_count: # 약품 투입 수가 최저 투입 수보다 작은 경우는 탐색 중지
        # print("중지")
        # print(arr)
        return

    if idx == D: # 약품 투입 행이 마지막 행 값보다 커지면
        if is_pass(arr, cnt): # 성능 검사를 통과하면 약품 투입 횟수 갱신
            min_count = cnt
            # print("count : ", min_count)
            # print(arr)
        return

    else:
        dfs(arr, idx+1, cnt)        # 약품 투입하지 않은 필름
        injection(arr, idx, 0)
        # print(arr)
        dfs(arr, idx+1, cnt+1)      # A 투입한 필름
        injection(arr, idx, 1)
        # print(arr)
        dfs(arr, idx+1, cnt+1)      # B 투입한 필름
        arr[idx][:] = films[idx][:] # 약품을 투입하기 전 필름으로 초기화
        # print(arr)

if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        D, W, K = map(int, input().split()) # 행 개수, 열 개수, 통과 개수
        global min_count
        min_count = K   # 최대 약품 투입 수는 합격 기준 K보다 크지 않으므로 최저 투입 횟수를 K값으로 초기화
        print(min_count)

        films = []
        for _ in range(D):
            films.append(list(map(int, input().split())))
        
        temp = copy.deepcopy(films)
        dfs(temp, 0, 0)
        print(f"#{i} {min_count}")


# import copy
# T = int(input())

# def check(b, d, w, k):
#     for j in range(w):
#         same = 1
#         for i in range(d-1):
#             if same == k:
#                 break
#             elif b[i][j] == b[i+1][j]:
#                 same += 1
#             else:
#                 same = 1
#         if same != k:
#             return False
#     print(b)
#     return True

# def dfs(depth, idx, board2, k):
#     global min_answer
#     if depth > min_answer:
#         return
#     if idx == d:
#         if check(board2, d, w, k):
#             print(board2)
#             min_answer = depth
#         return
#     else:
#         dfs(depth, idx+1, board2, k)
#         for y in range(w):
#             board2[idx][y] = 1
#         dfs(depth+1, idx+1, board2, k)
#         for y in range(w):
#             board2[idx][y] = 0
#         dfs(depth+1, idx+1, board2, k)
#         for y in range(w):
#             board2[idx][y] = board[idx][y]

# for test_case in range(1, T+1):
#     d, w, k = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(d)]
#     board2 = copy.deepcopy(board)
#     min_answer = k
#     dfs(0, 0, board2, k)
#     print(f'#{test_case} {min_answer}')