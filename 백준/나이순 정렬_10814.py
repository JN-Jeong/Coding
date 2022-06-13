N = int(input())

members = []
for i in range(N):
    age, name = input().split()
    members.append((int(age), name))
members.sort(key = lambda x : x[0])

for age, name in members:
    print(f"{age} {name}")


# N = int(input())

# members = []
# for i in range(N):
#     age, name = input().split()
#     members.append((int(age), name))

# for i in range(len(members)-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if members[i][0] < members[j][0]:
#             members[i], members[j] = members[j], members[i]

# for age, name in members:
#     print(f"{age} {name}")