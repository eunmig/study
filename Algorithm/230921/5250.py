import sys
sys.stdin = open('5250.txt')

import heapq

# 상하좌우 좌표
dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dijkstra(si, sj):
    # 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, si, sj))
    distance[si][sj] = 0

    while pq:
        # 현재시점 가장 짧은 노드 정보
        dist, now_x, now_y = heapq.heappop(pq)

        # 방문한 지점 + 누적거리가 더 짧게 방문한 적이 있으면 pass
        if distance[now_x][now_y] < dist:
            continue

        # 인접노트 델타확인
        for di, dj in dij:
            # 인덱스 범위 확인
            if 0 <= now_x + di < N and 0 <= now_y + dj < N:
                next_x = now_x + di
                next_y = now_y + dj

                # 누적거리구하기
                # 이동할때 높이 차이가 난다면 높이차만큼 더하기
                if arr[next_x][next_y] - arr[now_x][now_y] > 0:
                    new_cost = dist + 1 + (arr[next_x][next_y] - arr[now_x][now_y])
                else:
                    new_cost = dist + 1

                # 누적거리가 기존보다 크다면
                if distance[next_x][next_y] <= new_cost:
                    continue

                # new_cost 갱신
                distance[next_x][next_y] = new_cost
                heapq.heappush(pq, (new_cost, next_x, next_y))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 누적거리를 저장
    INF = int(1e9)  # 엄청 큰 최댓값 설정
    distance = [[INF] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {distance[N-1][N-1]}')