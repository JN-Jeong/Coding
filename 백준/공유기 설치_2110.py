"""
최대 값이 굉장히 크면 이진탐색을 사용해야함
X의 최대값이 1,000,000,000 -> 시간 복잡도가 log X가 돼야함
최대 gap, 최소 gap을 설정하여 이진탐색
"""

# 패캠 강의 풀이
N, C = list(map(int, input().split(" ")))

array = []
for i in range(N):
    array.append(int(input()))
array = sorted(array)

start = 1  # min_gap (array[1] - array[0] 으로 쓰면 오답)
end = array[-1] - array[0]  # max_gap
result = 0

while start <= end:
    mid = (start + end) // 2  # gap
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            count += 1
            value = array[i]

    if count >= C:  # C개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else:  # C개 이상의 공유기를 설치할 수 없는 경우
        end = mid - 1

print(result)
