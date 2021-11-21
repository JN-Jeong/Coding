# 미완료
n = int(input())
net = int(input())

connect = [1]
for i in range(net):
    a, b = map(int, input().split())
    if a in connect:
        connect.append(b)
    if b in connect:
        connect.append(a)

connect = set(connect)
print(connect)
print(len(connect)-1)