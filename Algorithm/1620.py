import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon_n = {}      # 숫자로 들어올 경우 -> 문자 출력
pokemon_s = {}      # 문자로 들어올 경우 -> 숫자 출력

for i in range(n):
    pokemon = input().rstrip()
    # 1부터 카운트
    pokemon_n[str(i+1)] = pokemon
    pokemon_s[pokemon] = i+1

for j in range(m):
    quiz = input().rstrip()
    if quiz.isdigit():      # 숫자라면
        print(pokemon_n[quiz])
    else:                   # 문자라면
        print(pokemon_s[quiz])