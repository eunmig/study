# 선택정렬
def selectionSort(a[], n):
    for i form 0 to n-2:
        a[i], ..., a[n-1] 원소 중 최소값 a[k] 찾음
        a[i]와 a[k] 교환


def selecionSort(a, n):
    # n-1 -> 0 to n-2까지
    # 미정렬원소가 하나 남은 상황에서는 마지막 원소가 가장 큰 값을 갖게 됨
    # 탐색을 종료하고 선택 정렬이 완료된다.
    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):
            # 원소 중 최소값 찾기
            if a[minIdx] > a[j]:
                minIdx = j
            # 최소값과 자리 교환
            a[i], a[minIdx] = a[minIdx], a[i]

# ----------------------------------------------
# 셀렉션 알고리즘
# k번째로 작은 원소를 찾는 알고리즘
def select(arr, k):
    for i in range(0, k):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = i
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr[k-1]
