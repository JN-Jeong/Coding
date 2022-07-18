N = int(input())
count = 0
while N >= 0: # 3으로 한번씩 빼고 5로 나누어 떨어지면 끝
    if N % 5 == 0:
        count += N // 5
        break

    N -= 3
    count += 1
else: # 3과 5로 나누어 떨어지지 않는다면 -1을 출력
    count = -1
print(count)