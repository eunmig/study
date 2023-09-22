def bfs(s):
    q = [s]
    visited = [0] * 101
    # 시작점은 방문처리
    visited[s] = 1

    max_number = s
    max_depth = 1

    while q:
        now = q.pop(0)

        # 갈 수 있는 지점 탐색
        for to in graph[now]:
            if visited[to]:
                continue

            # 기존 방문보다 한 번 더 이동
            visited[to] = visited[now] + 1

            # 한 단계 깊은 곳으로 가거나
            # 깊이는 같은데 숫자가 크다면
            # max 초기화
            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to

            q.append(to)
    return max_number

for tc in range(1, 11):
    n, start = map(int, input().split())
    # 임시로 전체 입력을 받음
    input_graph = list(map(int, input().split()))
    # 실제 사용할 인접 리스트 -> input_graph를 사용해서 만듦
    graph = [[] for _ in range(101)]
    for i in range(0, n, 2):
        f = input_graph[i]
        t = input_graph[i+1]
        graph[f].append(t)
    result = bfs(start)

    print(f'#{tc} {result}')