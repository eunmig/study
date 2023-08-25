import sys
sys.stdin = open('import.txt')

N = int(input())
game = [input() for _ in range(N)]
D_win = 0
P_win = 0

for i in game:
    if i == 'D':
        D_win += 1
    else:
        P_win += 1
    if abs(D_win - P_win) >= 2:
        break

print(D_win, P_win, sep=':')