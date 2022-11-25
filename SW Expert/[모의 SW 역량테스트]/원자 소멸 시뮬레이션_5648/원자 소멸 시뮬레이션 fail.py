"""
50개 중 24개 맞음
소멸한 원소가 남아있으면 안됨
3개 이상의 원소가 동시에 소멸되는 경우를 유의해야 함
어긋나는 원소의 경우를 유의해야 함 ((1,1,2,x), (0,1,3,x) -> 서로 (0,1), (1,1)이 되어서 만났으나 다시 멀어짐) -> dis 값이 ndis 값과 같으면 만난것?
"""


from collections import defaultdict


def solve():
    N = int(input())

    atoms = []
    for i in range(N):
        atoms.append(list(map(int, input().split())))
    
    print(atoms)
    # is_crash(atoms[0], atoms[1])

    # crashs = []
    crashs = defaultdict()
    visited = []
    for i in range(N-1):
        if (atoms[i][0], atoms[i][1]) in visited:
            print("방문했음", atoms[i][0], atoms[i][1])
            continue
        
        for j in range(i+1, N):
            if (atoms[j][0], atoms[j][1]) in visited:
                print("방문했음", atoms[j][0], atoms[j][1])
                continue

            res = is_crash(atoms[i], atoms[j])
            if res:
                loc, a, b = res
                if loc not in crashs:
                    crashs[loc] = []
                crashs[loc].append(a)
                crashs[loc].append(b)
                visited.append((atoms[j][0], atoms[j][1]))
        visited.append((atoms[i][0], atoms[i][1]))
    
    # print(crashs)
    # print(crashs.items())

    energy = 0
    for key in crashs.keys():
        for atom in list(set(crashs[key])):
            print(key, atom)
            energy += atom[2]
    
    return energy

def is_crash(atom1, atom2): # 좌표와 에너지 반환, solve 함수에서 만난 원자들의 좌표와 보유 에너지를 리스트에 저장하도록
    
    x1, y1 = atom1[0], atom1[1]
    x2, y2 = atom2[0], atom2[1]
    dis = (x1 - x2)**2 + (y1 - y2)**2 # 대각선 길이

    while True:
        if dis == 0: # 만났다면 좌표 반환
            print("만남")
            # print((x1, y1), (x2, y2)) # 1, 2 좌표 같음
            return (x1, y1), (atom1[0], atom1[1], atom1[3]), (atom2[0], atom2[1], atom2[3])
            
        nx1, ny1 = x1 + dx[atom1[2]], y1 + dy[atom1[2]]
        nx2, ny2 = x2 + dx[atom2[2]], y2 + dy[atom2[2]]
        ndis = (nx1 -nx2)**2 + (ny1 - ny2)**2
        # print(dis, ndis)
        if dis > ndis:
            x1, y1 = nx1, ny1
            x2, y2 = nx2, ny2
            dis = ndis
            # print("만날 예정")
        elif dis == ndis:
            print("엇갈림")
            # print((x1, y1), (x2, y2)) # 1, 2 좌표 같음
            return (x1, y1), (atom1[0], atom1[1], atom1[3]), (atom2[0], atom2[1], atom2[3])
        else:
            # print("안 만날 예정")
            return False



if __name__ == "__main__":
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    T = int(input())

    for i in range(1, T+1):
        print(f"#{i} {solve()}")