N = int(input())

sells = {}
for i in range(N):
    title = input()
    if title not in sells:
        sells[title] = 0
    sells[title] += 1

sells = sorted(sells.items(), key = lambda x:(-x[1], x[0]))
print(sells[0][0])
