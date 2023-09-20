# pivot값 보다 큰 값은 오른쪽, 작은 값은 왼쪽 집합에 위치
# 분류가 끝났을 경우,pivot의 요소를 두집합의 가운데에 위치

def partition(left, right):

    if left >= right:
        return

    pivot = left
    # i -> 첫번째 요소부터 j -> 마지막부터 거꾸로 내려가면서 비교
    i = left + 1
    j = right - 1

    while i <= j:
        # i가 pivot보다 작은값이면 +1 씩 이동하면서 비교
        while i <= j and arr[i] <= arr[pivot]:
            i += 1
        # j가 pivot보다 큰 값이면 -1씩 이동하면서 비교
        while i <= j and arr[j] >= arr[pivot]:
            j -= 1
        # pivot이 i보다 작거나 j보다 큰 경우, i와 j의 위치 바꿔주기
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 집합정렬이 끝난 후 pivot 위치 정렬
    # pivot 기준 왼쪽은 작은 값 오른쪽은 큰 값
    arr[pivot], arr[j] = arr[j], arr[pivot]

    # left < right가 될때까지 왼쪽, 오른쪽 나눠서 재귀호출 => 쪼개서 정렬될때까지 반복한다.
    partition(left, j)
    partition(j+1, right)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    left = 0
    right = len(arr)
    partition(left, right)
    result = arr[N//2]

    print(f'#{tc} {result}')
