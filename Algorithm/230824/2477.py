# 거꾸로된 'ㄱ'모양에서 오류
# 반례
# 1
# 2 5
# 3 5
# 1 1
# 4 2
# 1 4
# 4 3


import sys
sys.stdin = open('2477.txt')

fruit = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]
# print(arr)  [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]

# 바깥 사각형의 가로, 세로길이 -> 가로, 세로 길이중 가장 긴 길이
row_max, row_idx = 0, 0
col_max = 0
# 안쪽 작은 사각형의 가로, 세로 길이
row_min, col_min = 0, 0
for i in range(len(arr)):

    if arr[i][0] == 1 or arr[i][0] == 2:
        if row_max < arr[i][1]:
            row_max = arr[i][1]
            row_idx = i
            # print(row_max)
            # print(row_idx)
            row_min = arr[row_idx - 3][1]
            col_min = arr[row_idx - 4][1]
            # print(row_min)
            # print(col_min)

    else:
        if col_max < arr[i][1]:
            col_max = arr[i][1]

square = (row_max * col_max) - (row_min * col_min)

print(fruit * square)