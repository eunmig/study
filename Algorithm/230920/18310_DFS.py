# n : 시작정점, V : 정점 개수
def dfs(n, V, mtx):
    stack = []
    visited = [0] * (V+1)
    print(n, end='')
    # 시작점 방문 표시
    visited[n] = 1

    while True:
        # 모든 정점에 대하여
        for w in range(1, V+1):
            # n : 현재 정점, w : 방문확인할 정점
            # n과 w가 연결되어있고 방문하지 않았으면
            if mtx[n][w] == 1 and visited[w] == 0:
                # 시작점 stack에 append
                stack.append(n)
                # 정점 w 방문
                n = w
                print(n, end='')
                # 방문표시
                visited[n] = 1
                # 다시 for문 반복
                break

        # 방문하지 않은 정점이 없으면
        else:
            # 스택에 정점이 남아있다면
            if stack:
                n = stack.pop()
            # 스택이 빌때까지 반복
            else:
                break
    return

# N개의 정점, M개의 간선
V, E = map(int, input().split())
arr = list(map(int, input().split()))
mtx = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    # 인접 선 모두 표시
    mtx[v1][v2] = 1
    mtx[v2][v1] = 1

dfs(1, V, mtx)