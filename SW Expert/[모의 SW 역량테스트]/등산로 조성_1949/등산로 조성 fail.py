"""
[제약 사항]
1. 시간 제한 : 최대 51개 테스트 케이스를 모두 통과하는 데 C/C++/Java 3초, Python 15초
2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)
4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.
5. 지도에서 가장 높은 봉우리는 최대 5개이다.
6. 지형은 정수 단위로만 깎을 수 있다.
7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.


최대 봉우리 위치에서 bfs 탐색
최대 공사 가능 깊이 고려해야 함
높이가 같은 곳은 갈 수 없음

최대 공사 가능 깊이를 고려하여 갈 수 있는지 확인하는 함수가 필요할듯
입력으로 다음 위치, 현재 높이, 최대 공사 가능 깊이, 등산로 길이

1. 최대 봉우리들 위치 찾기
2. 최대 봉우리들 위치부터 bfs 또는 dfs 탐색 시작
3. 상하좌우에 최대 공사 가능 깊이를 고려하여 갈 수 있는 곳이 없다면 등산로 길이 반환 후 종료 (주의 : 딱 한 곳을 정해서 최대 K 깊이만큼 깎는 공사가 가능, 모든 위치에서 K 깊이만큼 깎을 수 있는 게 아님)
3-1. 현재 탐색된 최대 등산로 길이보다 크다면 갱신

"""


from copy import deepcopy


def solve():
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    # print(maps)

    max_ = 0
    for i in range(N):
        for j in range(N):
            if max_ < maps[i][j]:
                locs = []           
                max_ = maps[i][j]
            
            if max_ == maps[i][j]:
                locs.append((i, j, maps[i][j], K, 1))     # 가장 높은 봉우리들 위치와 현재 높이, 현재 최대 공사 가능 깊이, 현재 등산로 길이 저장
    
    # print(locs)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    max_count = 0

    for i, j, h, k, c in locs:
        visited = [[0] * N for _ in range(N)]
        q = list()
        q.append((i, j, h, k, c))
        visited[i][j] = 1
        # print()
        # print(q)

        while q:
            x, y, h, k, count = q.pop()
            
            if h < 0:
                continue

            if max_count < count:    # 현재 탐색된 최대 등산로 길이보다 크다면 갱신
                # print("갱신", count)
                # print(x, y, h, count)
                max_count = count

            for dir in range(4):
                nx, ny = x + dx[dir], y + dy[dir]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if visited[nx][ny] == 0 and h > maps[nx][ny] - k:       # 방문하지 않은 위치 and 현재 높이보다 낮은 높이를 방문
                    visited[nx][ny] = 1      # 방문 기록
                    if maps[nx][ny] >= h:    # 다음 위치의 높이가 현재 위치보다 크다면 현재 위치보다 1 낮게 깎음
                        nh = h - 1
                        q.append((nx, ny, nh, 0, count + 1))
                    else:
                        nh = maps[nx][ny]
                        q.append((nx, ny, nh, k, count + 1))
                    visited[nx][ny] = 0      # 방문 기록 초기화? (다른 경로에서 방문했던 기록을 없애줌)
        #             print(q)
        #             print(visited)

        # print(max_count)


    return max_count

if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print(f"#{i} {solve()}")