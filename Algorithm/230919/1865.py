def dfs(x):
    global max_percent, percent

    if x == N:
        if max_percent < percent:
            percent = max_percent

    if percent <= max_percent:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
    ```
    job[x][i]가 0일때는 곱하지않게 조건주기
    ```
            percent *= job[x][i]

            dfs(x+1)

            visited[i] = 0

            percent /= job[x][i]

    print(percent)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    job = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 비교할 최댓값 세팅
    max_percent = -10e9
    # 확률 최댓값 변수
    percent = 1

    result = (percent / 10000)

    dfs(0)
    print(f"#{tc} {'%.6f'%result}")
