def solution(n, lost, reserve):
    answer = 0
    
    clothes = [1] * n
    for l in lost:
        clothes[l-1] -= 1
    for r in reserve:
        clothes[r-1] += 1
        
    for i in range(n):
        if clothes[i] == 2:
            if i == 0:
                if clothes[i+1] == 0:
                    clothes[i+1] += 1
                    clothes[i] -= 1
            elif i == n-1:
                if clothes[i-1] == 0:
                    clothes[i-1] += 1
                    clothes[i] -= 1
            else:
                if clothes[i-1] == 0:
                    clothes[i-1] += 1
                    clothes[i] -= 1
                elif clothes[i+1] == 0:
                    clothes[i+1] += 1
                    clothes[i] -= 1
    print(clothes)
    
    for i in clothes:
        if i > 0:
            answer += 1
    return answer