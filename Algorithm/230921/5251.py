import sys
sys.stdin = open('5251.txt')

import heapq

def dijkstra(start):
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서 누적거리가 가장 짧은 노드에 대한 정보
        dist, now = heapq.heappop(pq)

        # 방문한 지점+ 누적거리가 더 짧게 방문한 적이 있으면 pass
        if distance[now] < dist:
            continue

        # 인접노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가는 누적거리
            new_cost = dist + cost

            # 누적거리가 기존보다 크다면
            if distance[next_node] <= new_cost:
                continue

            # new_cost 갱신
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 인접리스트
    graph = [[] for i in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])     # 단방향

    # 누적거리를 계속 저장
    INF = int(1e9)  # 엄청 큰 최댓값 설정
    distance = [INF] * (N+1)

    dijkstra(0)
    print(f'#{tc} {distance[N]}')