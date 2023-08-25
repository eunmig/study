T = int(input())

for tc in range(1, T+1):
    # 찾아야되는 노드
    N = int(input())
    # 노드 리스트
    node = [0] + list(map(int, input().split()))
    answer = 0

    for i in range(1, N+1):
        # 부모노드가 자식노드보다 클때 위치 바꿈
        while node[i//2] > node[i]:
            node[i//2], node[i] = node[i], node[i//2]
            # 다음 조상노드 검토
            i //= 2

    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    # 조상 노드 다 더하기
    # n의 부모부터 시작
    p = N // 2
    while p > 0:
        answer += node[p]
        p //= 2

    print(f'#{tc} {answer}')