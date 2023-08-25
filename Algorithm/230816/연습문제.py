# 라이브
def f(i, N, s):     # s: i-1 원소까지 부분집합의 합(포함된 원소의 합)
                    # t: 찾으려는 합
    global cnt
    cnt += 1
    if s == t:
        print(bit)
        return
    elif i == N:     # 남은 원소가 없는 경우
        return
    elif s > t:
        return

    else:
        bit[i] = 1      # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i])
        bit[i] = 0      # 부분집합에 A[i] 미포함
        f(i+1, N, s)
        return

# 부분집합 합이 10이 되는 경우
N = 10
A = [i for i  in range(1, N+1)]
f(0, N, 0)
bit = [0] * 3
print(cnt)

# ----------------------------------------------------
# 슬라이드
for solution(arr, k, cnt):
    if cnt != 10:
        return
    for i in range(1, k+1):
        if arr[i]:
            print(data[i], end=" ")
    print()

for make_candidates(arr, k, n, c):
    c[0] = 1    # 선택함
    c[1] = 0    # 선택안함
    return 2    # 생각할 수 있는 경우의 수

def backtracking(arr, k ,n, cut):
    if cut > 10:    #유망하지 않으면 가지치기
        return

    c = [0] * 2

    if k == n:
        solution(arr, k, cnt)
    else:
        k += 1
        ncandidates = make_candidates(arr, k, n, c)
        for i in range(ncandidates):
            arr[k] = c[i]
            if arr[k]:      # k 번째 원소를 선택한 경우
                # 총 합계에 k번쨰 원소의 값이 더해짐
                backtracking(arr, k, n, cnt + data[k])
            else:
                backtracking(arr, k, n ,cnt)

MAXCANDIDATES = 12
NMAX = 12

count = 0
arr = [0] * NMAX    # 각 원소를 사용할 것인지 체크

# 체크할 배열, 시작위치, 종료지지점, 합계
backtracking(arr, 0, 10, 0)

# ----------------------------------------------------
# 슬라이드_2
def powerset(arr, k, result):
    if sum(result) > 10:
        return

    if k == len(arr):
        if sum(result) == 10:
            print(result)
        return

    powerset(arr, K+1, result + arr[k])     # 포함하는 경우
    powerset(arr, K+1, result)              # 포함하지않는 경우


arr = list(range(1, 11))

# 원본배열, 사용한 원소 수, 사용할 원소를 담을 배열
powerset(arr, 0, [])

