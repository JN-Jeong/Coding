A, B = map(int, input().split())
C = int(input())

h = C // 60
m = C % 60

if (B+m) >= 60 and (B+m) % 60 >= 0:
    h += 1

print(f"{(A+h) % 24} {(B+m) % 60}")