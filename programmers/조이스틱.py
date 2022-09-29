# 와 이건 진짜 모르겠다
# 이해가 안된다
# 너무 어렵다
# 이게 레벨2?
# 난 대체 얼마나 찌끄레기인거지?

# def solution(name):
#     answer = 0
#     # print(ord('A')) # 65
#     # print(ord('Z')) # 90
    
#     pushs = [0] * len(name)
#     for i in range(len(name)): # 위아래 조작 최소값
#         pushs[i] = min(91 - ord(name[i]), ord(name[i]) - 65)
#         # print(pushs)
    
#     idx = 0
#     while True:
#         answer += pushs[idx]
#         pushs[idx] = 0
        
#         if sum(pushs) == 0:
#             break
            
#         left, right = 1, 1
#         while pushs[idx - left] == 0: # index를 왼쪽으로 옮기면서 눌려진 조이스틱을 찾을 때까지 left + 1
#             left += 1
            
#         while pushs[idx + right] == 0: # index를 오른쪽으로 옮기면서 눌려진 조이스틱을 찾을 때까지 right + 1
#             right += 1
            
#         if left < right: # left와 right 중 최소값을 찾아서 더함
#             answer += left
#             idx -= left
#         else:
#             answer += right
#             idx += right
    
#         print(pushs)

#     return answer


# def solution(name):
#     answer = 0
#     # print(ord('A')) # 65
#     # print(ord('Z')) # 90
    
#     min_move = len(name)
#     next_idx = 0
#     for i in range(len(name)): 
#         answer += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1) # 위아래 조작 최소값
        
#         next_idx = i + 1
#         while next_idx < len(name) and name[next_idx] == "A":
#             next_idx += 1
    
#         min_move = min(min_move, i + i + len(name) - next_idx, i + 2 * (len(name) - next_idx))
    
#     answer += min_move

#     return answer


def solution(name):
    answer = 0
    
    print(name, len(name))
    print("{} {} {} {}".format("i", "next_idx", "distance", "move"))
    move = len(name) - 1
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1) # 위아래 조작 최소값

        # next_idx : 위아래 조작 없는 알파벳 위치
        next_idx = i + 1
        while (next_idx < len(name)) and (name[next_idx] == "A"):
            next_idx += 1
        distance = min(i, len(name) - next_idx) # "A"를 찾는 distance?, 해당 문자의 위치 i랑 해당 문자 다음에서 A가 아닌 문자 뒤에서부터의 길이
        move = min(move, i + len(name) - next_idx + distance) # "A"가 아닌 문자를 왼쪽 방향으로 갔을 때 가장 적은 횟수

        print(i, next_idx, distance, move, answer)

    answer += move
    return answer


start_index = ord('A')
def solution(name):
    global name_len
    name_len = len(name) - 1
    return left_right_search([ord(i) for i in name], 0, 0)

def left_right_search(name, index, cost):
    print(f"index : {index}, cost : {cost}, name : {name}")
    c, name[index] = name[index], start_index # index 위치에 알파벳을 A로 변경해줌
    cost += min(c - ord("A"), ord("Z") - c + 1)
    name_set = set(name)
    name_set.remove(start_index)
    if len(name_set) == 0: # name_set으로 모든 name이 A가 되는지 확인하고 모든 name이 A가 되면 조이스틱의 조작 횟수를 반환하고 종료
        return cost
    right_index, right_distance = check_index(name, index, 1)
    left_index, left_distance = check_index(name, index, -1)
    right = left_right_search(name[:], right_index, cost + right_distance)  # 오른쪽으로 진행했을 때 조작 횟수가 최소인 경우를 갱신
    left = left_right_search(name[:], left_index, cost + left_distance)     # 왼쪽으로 진행했을 때 조작 횟수가 최소인 경우를 갱신
                                                                            # 각 index마다 각각의 방향으로 진행하면서 최소인 경우를 갱신하도록 함
    return min(left, right)

def check_index(name, index, term): # index 부터 왼쪽 또는 오른쪽으로 진행하면서
                                    # index와 A의 개수(distance)를 반환
                                    # => index는 A가 아닌 알파벳이 존재하는 index 값을 반환
                                    # => distance == index 위치로 부터 A가 아닌 알파벳이 존재하는 최소 거리
                                    # => distance 값이 조이스틱의 조작 횟수로 + 됨
                                    # => distance 값이 작은 방향으로 가야함
    distance = 0
    while name[index] == start_index: # start_index == "A"
        distance += 1
        index += term
        if index > name_len:
            index = 0
        elif index < 0:
            index = name_len
    return index, distance

name = "BBABAAAB"
name = "AAABAAAAAAAAAAAB" # len : 16
name = "AAABAAABAAAAAAAB" # len : 16
name = "AAABAAABAAAABAAA" # len : 16, r + l : 19-3, l : 15-3, r : 16-3

if __name__ == "__main__":
    solution(name)