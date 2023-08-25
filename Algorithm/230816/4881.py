import sys
sys.stdin = open('import.txt')

r, c = map(int, input().split())
cut = int(input())

# 자르는 위치 저장
# 초기값 0
row = [0, r]
col = [0, c]

for i in range(cut):
# 0일때는 가로, 1일때는 세로에 위치 저장
    cuting, line = map(int, input().split())
    if cuting == 1:
        row.append(line)
    else:
        col.append(line)

# 정렬해주기
row.sort()
col.sort()

# 빼서 최대 길이 구하기
row_cut = []
col_cut = []

for i in range(len(row)-1):
    row_cut.append(row[i+1] - row[i])
for j in range(len(col)-1):
    col_cut.append(col[j+1] - col[j])

# 최대 넓이 = 최대 가로 * 최대 세로
print(max(row_cut) * max(col_cut))