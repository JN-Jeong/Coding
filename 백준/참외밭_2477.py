K = int(input())

w = 0
h = 0
w_idx = 0
h_idx = 0
field = [list(map(int, input().split())) for _ in range(6)]

for i in range(len(field)):
    dir, length = field[i]
    if dir == 1 or dir == 2:    # 가로 길이
        if w < length:
            w = length
            w_idx = i
    elif dir == 3 or dir == 4:  # 세로 길이
        if h < length:
            h = length
            h_idx = i

sub_W = abs(field[(w_idx-1) % 6][1] - field[(w_idx+1) % 6][1])
sub_H = abs(field[(h_idx-1) % 6][1] - field[(h_idx+1) % 6][1])

print(field)
print(w_idx, h_idx)
print(field[(w_idx-1) % 6][1], field[(w_idx+1) % 6][1])
print(field[(h_idx-1) % 6][1], field[(h_idx+1) % 6][1])
# print(w, h)
# print(sub_W, sub_H)
ans = ((w*h) - (sub_W*sub_H)) * K
print(ans)