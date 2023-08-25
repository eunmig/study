import sys
sys.stdin = open('20205.txt')

N, K = map(int, input().split())
arr = [list(map(str, input().split())) for _ in range(N)]

# 2차원배열
for i in range(N):
    for l in range(K):  # 행을 K번 반복
        for j in range(N):
            for l in range(K):  # 열을 K번 반복
                print(arr[i][j], end=" ")
        print()
