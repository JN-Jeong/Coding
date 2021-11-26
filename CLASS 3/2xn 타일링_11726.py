n = int(input())

case = [1, 2]
for i in range(2, n):
    case.append(case[i-2] + case[i-1])

if n < 2:
    print(case[0]%10007)
elif n < 3:
    print(case[1]%10007)
else:
    print(case[-1]%10007)