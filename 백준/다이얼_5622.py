word = input()

dial = {}
i = 2
n = 65
while i < 10:
    if i == 7 or i == 9:
        for j in range(4):
            dial[chr(n+j)] = i
        i += 1
        n += 4
    else:
        for j in range(3):
            dial[chr(n+j)] = i
        i += 1
        n += 3

result = 0
for c in word:
    result += dial[c] + 1

print(result)