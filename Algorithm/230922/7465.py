# 부모 찾기
def find_set(x):
    if parents[x] == x:
        return x

    # 부모를 찾을때까지 반복
    parents[x] = find_set(parents[x])
    return parents[x]

# 부모 병합
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x > y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T+1):
    # n : 사람 수, m : 사람의 관계 수
    n, m = map(int, input().split())
    # 부모가 누군지 저장하는 변수
    parents = [i for i in range(n+1)]

    for i in range(m):
        v1, v2 = map(int, input().split())
        # 루트가 같으면 continue
        if find_set(v1) == find_set(v2):
            continue
        union(v1, v2)

    # 같은 관계는 반복해서 주어지지 않는다.
    root = set()

    # 총 연결 개수 찾기
    # 편의상 1번부터 n번까지 번호가 붙어져 있다고 가정
    for i in range(1, n+1):
        root.add(find_set(i))

    print(f'#{tc} {len(root)}')