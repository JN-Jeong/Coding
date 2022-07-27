def solution(n, arr1, arr2):
    answer = []
    
    answer = []
    for s1, s2 in zip(arr1, arr2):
        temp = bin(s1 | s2).split('0b')[1]
        while len(temp) < n:
            temp = '0' + temp
        temp = temp.replace('1', '#').replace('0', ' ')
        answer.append(temp)
    
    print(answer)
            
    return answer