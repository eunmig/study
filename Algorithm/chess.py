n, m = map(int, input().split())

board = []
result = []

for _ in range(n):
    board.append(input())

# 보드의 모든 가능한 8x8 구역을 탐색
for i in range(n-7):
    for j in range(m-7):

        draw1 = 0  # 좌상단이 'B'로 시작하는 패턴
        draw2 = 0  # 좌상단이 'W'로 시작하는 패턴

        # 현재 8x8 구역의 각 셀을 확인
        for a in range(i, i+8):
            for b in range(j, j+8):
                # (a + b)가 짝수인 경우
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':  # 셀이 'B'가 아니면
                        draw1 += 1
                    if board[a][b] != 'W':  # 셀이 'W'가 아니면
                        draw2 += 1
                else:  # (a + b)가 홀수인 경우
                    if board[a][b] != 'W':  # 셀이 'W'가 아니면
                        draw1 += 1
                    if board[a][b] != 'B':  # 셀이 'B'가 아니면
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

# 최소 출력
print(min(result))