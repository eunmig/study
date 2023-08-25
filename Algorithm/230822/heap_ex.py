def deq():
    global last
    tmp = heap[1]           # 루트백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식노드와 비교
    c = p * 2               # 왼쪽 자식노드 (비교할 자식노드 번호)
    while c <= last:        # 자식노드가 하나라도 있으면
        # 오른쪽 자식노드도 있고 오른쪽 자식노드가 더 크면
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1  # 비교 대상이 오른쪽 자식 노드
        # 자식 노드가 더 크면 최대힙 규칙에 어긋나므로
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c       # 자식노드를 새로운 부모노드로 바꿈
            c = p *2    # 왼쪽 자식노드 번호를 계산
        else:           # 부모노드가 더 크면
            break       # 비교 중단

    return tmp

heap = [0] * 100
last = 0