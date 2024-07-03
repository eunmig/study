import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 다중조건으로 sort
arr.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(n):
    if arr[i][0] == k:
        index = i

for j in range(n):
    if arr[index][1:] == arr[j][1:]:
        print(j+1)
        break