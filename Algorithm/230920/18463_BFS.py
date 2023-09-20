# s: 시작정점, e : 마지막 정점
def bfs(s, e):
    visited = [0] * (e+1)
    # 큐 생성
    queue = []
    # 시작점 인큐
    queue.append(s)
    # 시작점에 방문표시
    visited[s] = 1

    # 큐에 정점이 남아있으면
    while queue:
        # 디큐
        now = queue.pop(0)
        # 정점에서 할일 방문정점 출력
        print(now, end= ' ')

        # 인접한 정점중에
        for next in mtx[now]:
            # 방문하지 않은 정점이 있다면
            if visited[next] == 0:
                # 큐에 넣기
                queue.append(next)
                visited[next] = visited[now] + 1


# N개의 정점, M개의 간선
N, M = map(int, input().split())
arr = list(map(int, input().split()))
mtx = [[] for _ in range(N+1)]

for i in range(M):
    v1, v2 = arr[i*2], arr[i*2+1]
    # 방향이 없는경우
    mtx[v1].append(v2)
    mtx[v2].append(v1)

bfs(1, 7)