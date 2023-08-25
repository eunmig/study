T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bug = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for k in range(M):
                for l in range(M):
                    kill += arr[i+k][j+l]

            bug.append(kill)

    print(f'#{tc}', max(bug))