nums = list(map(int, input().split()))

dices = {}

for n in nums:
    if n not in dices:
        dices[n] = 0
    dices[n] += 1

dices = sorted(dices.items(), key = lambda x : (x[1], x[0]), reverse=True)      # 눈의 종류가 key값(x[0]), 개수가 value값(x[1]), 개수로 정렬한 후 종류로 내림차순 정렬(reverse=True)

if len(dices) > 2:                          # 눈의 종류가 2개 초과라면
    print(dices[0][0] * 100)
elif len(dices) > 1:                        # 눈의 종류가 2개 이하 1개 초과라면
    print(1000 + dices[0][0] * 100)
else:                                       # 눈의 종류가 1개 이하라면
    print(10000 + dices[0][0] * 1000)