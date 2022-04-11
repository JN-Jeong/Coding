# # 첫 접근
# # 모든 부분집합을 만들고 계산
# # 결과는 실행 시간 초과...
# def solution(number, k):
#     answer = ''
    
#     subsets = []
#     for i in range(1 << len(number)):
#         subset = []
#         for j in range(len(number)):
#             if i & 1 << j:
#                 subset.append(number[j])
        
#         if len(subset) == (len(number) - k):
#             subsets.append(subset)
        
#     max_num = 0
#     for i in range(len(subsets)):
#         num = int(''.join(subsets[i]))
#         if max_num < num:
#             max_num = num
#             answer = str(num)
        
#     return answer

# # 두 번째 접근
# # 차례대로 list[idx:idx+k]를 확인하여
# # 범위 내에 list[idx] 값보다 큰 수가 존재하면 list[idx] 값을 제거
# # 실행 시간 초과로 실패
# def solution(number, k):
#     answer = ''
    
#     # 앞자리 0 ~ k-1 index의 숫자가 만약 k+1 index의 숫자보다 작다면
#     # 0 ~ k-1 index의 숫자들을 없애주면 됨
#     # 하지만 0 ~ k-1 index의 숫자들 중 k+1 ~ index의 숫자보다 큰 숫자가 존재하면
#     # 

#     print(number, k)
    
#     idx = 0
#     values = [] # 제거할 숫자값
#     while idx < len(number):
#         if k < 0:
#             break
        
#         if len(number[idx:]) == k:
#             for i in range(k):
#                 values.append(number[i+idx])
#             k = 0
#             break
        
#         for i in range(k):
#             if int(number[idx]) < int(number[idx+1+i]):
#                 # number = number[:idx] + number[idx+1:] # 너무 오래걸림
#                 values.append(number[idx])
#                 k -= 1
#                 break

#         idx += 1

#     print(values)
#     numbers = []
#     for n in number:
#         numbers.append(n)

#     for n in values:
#         numbers.remove(n)
    
#     print(numbers)
#     answer = ''.join(numbers)

#     return answer


def solution(number, k):
    answer = []
    
    for n in number:
        if not answer: # 초기 값 추가
            answer.append(n)
            continue
        
        while k > 0 and answer and answer[-1] < n: # 큰 값을 앞에 두도록 만들어줌
            answer.pop()
            k -= 1
        answer.append(n)
        # print(answer, k)
    
    if k > 0: # 남은 k 값만큼 answer 리스트의 마지막 원소 제거
        for _ in range(k):
            answer.pop()
            
    return ''.join(answer)


if __name__ == "__main__":
    # number = "1924"
    # k = 2
    number = "4177252841" 
    k = 4

    print(solution(number, k))