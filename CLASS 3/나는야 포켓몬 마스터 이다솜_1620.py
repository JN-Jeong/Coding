import sys

N, M = map(int, sys.stdin.readline().split())

pokemon_dict = {}
rev_pokemon_dict = {}
for i in range(1, N+1):
    pokemon = input()
    pokemon_dict[i] = pokemon
    rev_pokemon_dict[pokemon] = i

for i in range(M):
    question = input()
    if question.upper() == question.lower(): # 숫자
        print(pokemon_dict[int(question)])
    else: # 문자
        print(rev_pokemon_dict[question])