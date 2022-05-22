# # 시간 초과
# n = int(input())

# def pibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     return pibo(n-1) + pibo(n-2)

# print(pibo(n))


# 패캠 강의 풀이
n = int(input())
a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n = n -1

print(a)

"""
0 1 1 2 3 5 8
a b
  a b
    a b
      a b
        a b
          a b
"""