n = int(input())
n_num = sorted(list(map(int, input().split())))
m = int(input())
m_num = list(map(int, input().split()))

# m개의 카드에서 상근이가 가지고 있는 숫자카드이면
# 1을 출력 아니면 0을 출력 -> 공백으로 구분해서 출력
# 시간 초과 error
#for i in m_num:
#    if i in n_num:
#        print(1, end=' ')
#    else:
#        print(0, end=' ')

# 이진탐색 -> 탐색시간 절약으로 시간초과 에러 해결
def binary_search(start, end, key):
    while start <= end:
        mid = (start + end) // 2
        if n_num[mid] == key:
            return 1            # 검색성공 1 출력
        # key가 middle 보다 작다면 end 조정해서 오른쪽 탐색
        elif n_num[mid] > key:
            end = mid - 1
        # key가 middle 보다 크다면 start 조정해서 왼쪽 탐색
        else:
            start = mid + 1
    return 0                    # 검색실패 0 출력


for i in m_num:
    print(binary_search(0, n-1, i), end=' ')