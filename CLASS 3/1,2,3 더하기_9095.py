T = int(input())

case = [1,2,4]
for i in range(3, 11):
    case.append(case[i-3] + case[i-2] + case[i-1])

for _ in range(T):
    n = int(input())
    print(case[n-1])