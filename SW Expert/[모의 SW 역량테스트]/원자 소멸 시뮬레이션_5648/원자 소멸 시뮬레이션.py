"""
1. 원자들의 수 N 은 1,000개 이하이다. (1≤N≤1,000)
2. 각 원자들의 보유 에너지 K 는 1 이상 100 이하이다. (1≤K≤100)
3. 원자들의 처음 위치 [x, y] 는 -1,000 이상 1,000 이하의 정수로 주어진다. (-1,000≤x,y≤1,000)
4. 원자들은 2차원 평면 위에서 움직이며 원자들이 움직일 수 있는 좌표의 범위에 제한은 없다.
5. 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)로 주어진다.
6. 원자들은 동시에 1초에 이동 방향으로 1만큼 이동한다.
7. 원자들의 최초 위치는 서로 중복되지 않는다.
8. 원자들은 2개 이상의 원자들이 서로 충돌할 경우 보유한 에너지를 방출하면서 바로 소멸된다.
9. 원자들은 이동 방향은 처음에 주어진 방향에서 바뀌지 않는다.
10. 원자들이 충돌하여 소멸되며 방출되는 에너지는 다른 원자의 위치나 이동 방향에 영향을 주지 않는다.
"""


def solve():
    N = int(input())

    atoms = []
    for loc in range(N):
        atoms.append(list(map(int, input().split()))) # atoms 리스트에 입력받은 원자들 저장
    
    # 0.5씩 이동하도록 만듬
    dx = [0, 0, -0.5, 0.5]
    dy = [0.5, -0.5, 0, 0]

    def move(atom): # 입력받은 원자를 0.5 이동시킨 후 반환
        nx = atom[0] + dx[atom[2]]
        ny = atom[1] + dy[atom[2]]
        return [nx, ny, atom[2], atom[3]]
        

    def crash(atom): # 충돌이 발생한지 확인하기 위해 딕셔너리로 고유한 위치(key)에 원자들(value)을 저장
        loc = atom[0], atom[1]
        if not (loc) in atom_dict:
            atom_dict[loc] = []
        atom_dict[loc].append(atom)

    count = 0
    energy = 0
    while True:
        if len(atoms) < 2:
            break
        
        atom_dict = {}
        atoms = list(map(move, atoms))  # atoms 리스트에 원자들의 위치 갱신 (0.5씩 원자들을 주어진 방향으로 이동)
        list(map(crash, atoms))         # atoms 리스트에서 고유한 위치들로 딕셔너리에 원자들을 저장, 고유한 위치에 저장된 원자가 많다면 충돌한 원소들
        # print(atom_dict)
        atoms = []                      # 소멸하지 않은 원자들을 저장하기 위해 초기화

        for loc in atom_dict:
            if len(atom_dict[loc]) > 1: # 동일한 위치에 원자가 여러개 존재한다면 atoms 리스트에 추가하지 않고 에너지를 증가시킴
                atom = atom_dict[loc]
                for e in atom:
                    energy += e[3]

            else:
                atom = atom_dict[loc]
                x, y = atom[0][0], atom[0][1]

                if x < -1000 or x > 1000 or y < -1000 or y > 1000:  # 원자들이 처음 위치할 수 있는 범위 밖으로 나가면 삭제
                    continue
                else:                                               # 소멸하지 않은 원소들은 다시 atoms 리스트에 저장
                    atoms.append(atom[0])
        count += 1
    print("count : ", count)
    return energy


            
if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print(f"#{i} {solve()}")