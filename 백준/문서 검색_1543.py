doc = input()
word = input()

result = 0
i = 0
while i < len(doc):
    if doc[i:i+len(word)] == word:
        result += 1
        i += len(word)
    else:
        i += 1

print(result)