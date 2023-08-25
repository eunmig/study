import sys
sys.stdin = open('24049.txt')

# 가로, 세로 길이 받기
N, M = map(int, input().split())
# 왼쪽 가장자리 - 0 : 노란색, 1 : 빨간색
col = list(map(int, input().split()))
# 위쪽 가장자리 - 0 : 노란색, 1 : 빨간색
row = list(map(int, input().split()))
flower = [[0] *(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    flower[i][0] = col[i-1]
    for j in range(1, M+1):
        flower[0][j] = row[j-1]

for i in range(1, N+1):
    for j in range(1, M+1):
        # row = col -> 노란색
        if flower[i-1][j] == flower[i][j-1]:
            flower[i][j] = 0
        else:
            # row != col -> 빨간색
            flower[i][j] = 1

print(flower[N][M])

