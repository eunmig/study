'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, V):  # s : 시작정점, V : 마지막 정점
    visited = [0] * (V+1)   # visited 생성
    q = []                  # 큐 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 방문표시
    while q:                # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)        # dequeue
        print(t)            # 방문한 정점에서 할일
        for w in range(1, V+1):  # 인접한 정점 중 inqueue되지 않은 정점 w가 있으면
            if adj_m[t][w] == 1 and visited[w] == 0:
                q.append(w)     # w inqueue, inqueue 되었음을 표시
                visited[w] = visited[t] + 1


V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트 -----------------------------
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1   # 방향이 없는 경우

bfs(1, 7)