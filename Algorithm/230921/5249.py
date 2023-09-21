import sys
sys.stdin = open('5249.txt')

def find_set(x):
    if parent[x] == x:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # x = y이면 싸이클 발생
    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 현재 방문한 정점수
    cnt = 0
    # 가중치의 합
    sum_weight = 0

    # 인접행렬
    edge = []
    for _ in range(M):
        f, t, w = map(int, input().split())
        edge.append([f, t, w])

    # w를 기준으로 정렬
    edge.sort(key=lambda x : x[2])

    # 싸이클 발생여부 union find로 해결
    parent = [i for i in range(N+1)]


    for f, t, w in edge:
        # 싸이클이 발생하지 않는다면
        if find_set(f) != find_set(t):
            cnt += 1
            sum_weight += w
            union(f, t)

            # MST 구성이 끝나면
            if cnt == N:
                break
    print(f'#{tc} {sum_weight}')