"""
https://softeer.ai/practice/6288
금고털이
"""

import sys


def solution():
    answer = 0
    w, n = map(int, input().split())
    materials = []

    for _ in range(n):
        material_weight, material_price = map(int, input().split())
        materials.append([material_weight, material_price])

    materials.sort(key=lambda x: x[1], reverse=True)
    # print("@", materials)

    for weight, price in materials:
        if w > weight:
            answer += weight * price
            w -= weight
        else:
            answer += w * price
            break

    return answer


print(solution())
