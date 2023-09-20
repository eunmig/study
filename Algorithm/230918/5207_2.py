def binarySearch(start, end, key, arr):
    global cnt

    left = 0
    right = 0

    while start <= end:
        mid = (start + end) // 2

        # 같은 방향으로 연속적으로 들어갔을 경우 탐색종료
        if left == 2 or right == 2:
            break
        elif arr[mid] == key:
            cnt += 1
            return mid
        # key가 mid 보다 작을경우
        # 왼쪽방향 +1, 오른쪽방향 0으로 초기화
        elif arr[mid] > key:
            end = mid - 1
            left += 1
            right = 0
        # key가 mid 보다 클 경우
        # 오른쪽방향 +1, 왼쪽방향 0으로 초기화
        else:
            start = mid + 1
            right += 1
            left = 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for num in range(M):
        binarySearch(0, N-1, B[num], A)

    print(f'#{tc} {cnt}')