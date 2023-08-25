N = int(input())

cnt = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        # 가로*세로 1인 정사각형
        # 가로*세로가 곱한 넓이가 주어진 N보다 클수는 없다.
        if i * j <= N:
            cnt += 1

print(cnt)