import sys
sys.stdin = open('4108.txt')

while True:
    R, C = map(int, input().split())

    text = [list(map(str, input())) for _ in range(R)]
    # 상하좌우
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    # 대각선
    ci = [1, 1, -1, -1]
    cj = [-1, 1, -1, 1]
    if R == C == 0:
        break

    for row in range(R):
        for col in range(C):
            if text[row][col] == '*':
                text[row][col] = '*'
            else:
                bomb = 0
                for k in range(4):
                    r1, r2 = row + di[k], col + dj[k]
                    c1, c2 = row + ci[k], col + cj[k]
                    if 0 <= r1 < R and 0 <= r2 < C and text[r1][r2] == '*':
                        bomb += 1
                    if 0 <= c1 < R and 0 <= c2 < C and text[c1][c2] == '*':
                        bomb += 1

                text[row][col] = str(bomb)

    for i in range(R):
        print(*text[i], sep="")




