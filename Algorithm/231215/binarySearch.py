def binarySearch(a, n, key):
    start = 0
    end = n-1

    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return true         # 검색성공
        # key가 middle 보다 작다면 end 조정해서 오른쪽 탐색
        elif a[middle] > key:
            end = middle - 1
        # key가 middle 보다 크다면 start 조정해서 왼쪽 탐색
        else:
            start = middle + 1
    return false                # 검색실패