# 열 슬라이싱 방법을 배움
# list(zip(*str_map))
# => *로 리스트를 언패킹(unpacking)하면 각 행들을 리스트로 분리함
# => 분리된 리스트들을 zip함수로 동일한 인덱스에 있는 값들로 합침
# => 생성된 zip 오브젝트를 list로 형변환

def solve():
    N, M = map(int, input().split())

    str_map = []
    for _ in range(N):
        str_map.append(list(input()))

    for i in range(N): # 가로
        cols = []
        for j in range(N-M+1):
            rows = list(str_map[i][j:M+j]) # 행
            # print("rows : ", rows)
            cols = list(zip(*str_map[j:M+j]))[i] # 열 (※열 슬라이싱 방법)
            # print("cols : ", cols)

            # M이 홀수인 경우를 대비하여 [-(M//2):]으로 슬라이싱 해줌
            if list(rows[:M//2]) == list(reversed(rows[-(M//2):])):
                return ''.join(rows)
            if list(cols[:M//2]) == list(reversed(cols[-(M//2):])):
                return ''.join(cols)


if __name__ == "__main__":
    
    T = int(input())
    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))