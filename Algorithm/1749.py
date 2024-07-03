import sys
input = sys.stdin.readline

# n : 세로, m : 가로
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 누적합 구하기
sum_arr = [[0] * (m+1) for _ in range (n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i][j-1] + sum_arr[i-1][j] - sum_arr[i-1][j-1]

# 구간합 구하기
max_sum = -10e9
for x1 in range(1, n+1):
    for y1 in range(1, m+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1, m+1):
                value = sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1]
                if value > max_sum:
                    max_sum = value

print(max_sum)