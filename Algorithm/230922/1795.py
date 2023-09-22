import sys
sys.stdin = open('1795.txt')

import heapq

def dijkstra(start, x):
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))

    INF = int(1e9)  # 엄청 큰 최댓값 설정
    distance = [INF] * (n+1)
    distance[start] = 0

    while pq:
        # 현재 시점에서 누적거리가 가장 짧은 노드
        dist, now = heapq.heappop(pq)

        # 도착하면 종료하고 현재 거리값 return
        if now == x:
            return distance[now]

        # 방문한 지점 + 누적거리가 더 짧게 방문한 적이 있으면 pass
        if distance[now] < dist:
            continue

        # 인접노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가는 누적거리
            new_cost = dist + cost

            # 누적거리가 기존보다 작다면
            if distance[next_node] <= new_cost:
                continue

            # new_cost 갱신
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


T = int(input())
for tc in range(1, T+1):
    # n : 집, m: 간선, x : 집
    n, m, x = map(int, input().split())

    # 인접리스트
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        # 출발, 도착, 가중치
        f, t, w = map(int, input().split())
        graph[f].append([t, w])


    # 자기자신까지 누적거리 저장
    arrived = [0] * (n+1)
    for k in range(1, n+1):
        # 왕복 거리
        arrived[k] += dijkstra(k, x)
        arrived[k] += dijkstra(x, k)

    result = max(arrived)
    print(f'#{tc} {result}')