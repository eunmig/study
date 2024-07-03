T = int(input())

for tc in range(1, T+1):
    # 1부터 12까지의 원소를 숫자를 원소로 가진 집합 arr
    arr = [i for i in range(1, 13)]
    # n개의 원소를 갖고 있고 원소의 합이 k인 부분집합의 개수
    count = 0
    n, k = map(int, input().split())

    # 공집합 포함
    # 부분집합의 개수
    for i in range(1<<12):
        # 빈 리스트, 원소의 합 세팅
        set_lst = []
        set_sum = 0
        # 12개의 원소만큼 반복
        for j in range(12):
            if i & (1<<j):
                set_lst.append(arr[j])
                set_sum += arr[j]
        if len(set_lst) == n and set_sum == k:
            count += 1

    print(f'#{tc} {count}')