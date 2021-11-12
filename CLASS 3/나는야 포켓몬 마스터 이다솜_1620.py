import sys

N, M = map(int, sys.stdin.readline().split())

pokemon_dict = {}
for i in range(1, N+1):
    pokemon = input()
    pokemon_dict[i] = pokemon

rev_pokemon_dict = {}
for key, value in pokemon_dict.items():
    rev_pokemon_dict[value] = key

for i in range(M):
    question = input()
    if question.upper() == question.lower(): # 숫자인지 확인
        print(pokemon_dict[int(question)])
    else: #
        print(rev_pokemon_dict[question])