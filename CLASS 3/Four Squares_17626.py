n = int(input())

squares = []
for i in range(223, 0, -1):
    squares.append(i**2)

num_list = [50000 for _ in range(n + 1)]
num_list[0] = 0
for j in range(n + 1):  # 입력 값 n (거스름돈)
    for i in range(len(squares)):  # 제곱수 종류 (동전 종류)
        if squares[i] <= j and num_list[j - squares[i]] + 1 < num_list[j]:
            num_list[j] = num_list[j - squares[i]] + 1

print(num_list[n])
