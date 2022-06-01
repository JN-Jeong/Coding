S = input()

length = 0
result = []
while length < len(S):
    for i in range(len(S) - length):
        result.append(S[i : i + length + 1])
    length += 1

print(len(set(result)))