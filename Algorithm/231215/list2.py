# 1. 행 우선 순회
for i in range(n):          # i행의 좌표
    for j in range(m):      # j행의 좌표
        print(arr[i][j])        # 필요한 연산 수행

# 2. 열 우선 순회
for j in range(m):          # j행의 좌표
    for i in range(n):      # i행의 좌표
        print(arr[i][j])        # 필요한 연산 수행

# 3. 지그재그 순회
for i in range(n):          # i행의 좌표
    for j in range(m):      # j행의 좌표
        # j + m-1-2*j = m-1-j
        # i%2 -> 홀수일때만 거꾸로 순회
        print(arr[i][j + (m-1-2*j) * (i%2)])

# 4. 델타를 이용한 2차 배열 탐색
arr[0, .., N-1][0, .., N-1]     # NxN 배열
# 상하좌우 4방향
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(N):
        for k in range(4):      # 상하좌우 4방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj])

# 5. 전치 행렬
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]     # 3*3 행렬

for i in range(3):          # i : 행의 좌표, len(arr)
    for j in range(3):      # j : 열의 좌표, len(arr[0)
        if i < j :
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]