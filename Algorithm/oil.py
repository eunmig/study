from collections import deque


def solution(land):
    answer = 0
    # 행, 열
    n, m = len(land), len(land[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 각 열의 기름 총량
    result = [0 for i in range(m)]
    # 방문 기록
    visited = [[0 for _ in range(m)] for _ in range(n)]

    def bfs(oil):
        a, b = oil
        # 연결된 석유 초기 개수
        cnt = 1
        # 시작 위치 방문 표시
        visited[a][b] = 1

        q = deque()
        # 시작위치 큐 추가
        q.append(oil)

        # 석유가 존재하는 열 저장 (중복 방지)
        oil_col = set()
        oil_col.add(b)

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 범위를 벗어나지 않으면서 방문하지않았고 석유가 있다면
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    q.append((nx, ny))  # 새로운 좌표 큐 추가
                    visited[nx][ny] = 1  # 방문 표시
                    cnt += 1  # 연결된 석유 +1
                    oil_col.add(ny)  # 석유가 존재하는 열 저장

        # 탐색이 끝난 후
        # 각 열의 석유 총량 업데이트
        for c in oil_col:
            result[c] += cnt

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs((i, j))  # 재탐색

    answer = max(result)

    return answer