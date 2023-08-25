import sys
sys.stdin = open('2167.txt')

# 배열의 크기 정수로 받기
N, M = map(int, input().split())
# 배열 리스트로 받기
num_list = [list(map(int, input().split())) for _ in range(N)]
# 반복횟수
K = int(input())

for _ in range(K):
    # 좌표
    i, j, x, y = map(int, input().split())
    # i,j부터 x,y까지 덧셈 카운트
    count = 0

    # i,j부터 x,y까지 탐색
    for row in range(i-1, x):
        for col in range(j-1, y):
            count += num_list[row][col]

    print(count)