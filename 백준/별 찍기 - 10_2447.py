"""
어렵다...
재귀 함수를 호출하자마자 출력하는 것이 아니라 *을 원소로 가진 리스트로 반환하는 발상이 가능해야 함
"""

N = int(input())

def pattern(n):
    if n == 1:
        return ['*']

    stars = pattern(n//3)
    patterns = []

    for star in stars:
        patterns.append(star*3)
    for star in stars:
        patterns.append(star + ' ' * (n//3) + star)
    for star in stars:
        patterns.append(star*3)

    print(patterns)

    return patterns

# pattern(N)
print('\n'.join(pattern(N)))