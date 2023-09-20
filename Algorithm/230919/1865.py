def dfs(x):
    global max_percent, percent

    if x == N:
        if max_percent < percent:
            max_percent = percent

    if percent <= max_percent:
        return

    for i in range(N):
        if visited[i] == 0:
            # job[x][i]가 0일 때 건너뛰기
            if job[x][i] == 0:
                continue

            visited[i] = 1
            percent *= job[x][i]
            dfs(x + 1)
            visited[i] = 0
            percent /= job[x][i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    job = [list(map(int, input().split())) for _ in range(N)]
    # 100으로 나눠서 확률 계산
    for i in range(N):
        for j in range(N):
            job[i][j] = job[i][j] / 100

    visited = [0] * N
    # 비교할 최댓값 세팅
    max_percent = -10e9
    percent = 1

    dfs(0)

    result = "%.6f" % (max_percent * 100)
    print(f"#{tc} {result}")
