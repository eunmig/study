import sys
sys.stdin = open('3041.txt')

R, C, ZR, ZC = map(int, input().split())
arr = [input() for _ in range(R)]
# 스캔 결과 리스트
scanner = []

for i in range(R):
    # 각 행의 내용을 저장한 리스트
    row = []
    # 행*ZR, 열*ZC
    for j in range(C):
        row.append(arr[i][j]*ZC)
    for _ in range(ZR):
        scanner.append(row)

for k in scanner:
    print(''.join(k))
