BubbleSort(a, N):                   # 정렬할 배열과 배열의 크기
    for i : N-1 -> 1                # 정렬될 구간의 끝
        for j : 0 -> i-1            # 비교할 원소 중 왼쪽 원소의 인덱스
            if a[j] < a[j+1]        # 왼족 원소가 더 크면
                a[j] <-> a[j+1]     # 오른쪽 원소와 교환



def BubbleSort(a, N):               # 정렬할 list, N 원소 수
    for i in range(N-1, 0, -1):     # 범위의 끝 까지
        for j in range(0, i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]