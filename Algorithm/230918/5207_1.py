def binarySearch(key):
    start = 0
    end = N - 1
    # 한쪽방향으로 두번 들어가는 순간 종료
    check = 0

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == key:
            return True
        elif A[mid] > key:
            # 이미 check가 한방향으로 들어갔을경우 현재의 경우까지 더해지면
            # 연속적으로 같은 방향으로 들어가게되어 탐색종료
            if check == 1:
                break
            check = 1
            end = mid - 1
        else:
            # 같은 방향으로 두번 연속 탐색종료
            if check == 2:
                break
            check = 2
            start = min + 1
    return False

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 리스트 정렬
    A = sorted(A)

    total = 0
    for num in B:
        total += binarySearch(num)

    print(f'#{tc} {total}')
