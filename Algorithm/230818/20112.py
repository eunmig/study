import sys
sys.stdin = open('20112.txt')

N = int(input())
word = [list(map(str, input())) for _ in range(N)]
babo = True
for row in range(N):
    for col in range(N):
        if word[row][col] == word[col][row]:
            continue
        else:
            babo = False
            break

if babo:
    print('YES')
else:
    print('NO')