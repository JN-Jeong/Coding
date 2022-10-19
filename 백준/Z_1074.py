# 패캠 강의 풀이
N, r, c = map(int, input().split())

result = 0
def solve(n, x, y):
    global result
    if not (x <= r < x + n and y <= c < y + n):     # 찾는 위치를 벗어나면 탐색 중단
        result += n ** 2
        # print("중단")
        return

    if x == r and y == c:       # 찾는 위치이면 값 출력 후 종료
        print(int(result))
        exit(0)

    if n == 1:      # 2 x 2 크기가 될 때까지 재귀함수 호출
        result += 1
        return

    # 순서 중요 (2, 1, 3, 4사분면)
    solve(n/2, x, y)                # 4등분 (2사분면)
    solve(n/2, x, y + n/2)          # 4등분 (1사분면)
    solve(n/2, x + n/2, y)          # 4등분 (3사분면)
    solve(n/2, x + n/2, y + n/2)    # 4등분 (4사분면)

solve(2**N, 0, 0)