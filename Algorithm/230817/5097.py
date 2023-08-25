T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    # M번 반복
    for _ in range(M):
        # 리스트에 저장된 첫번쨰원소 pop하고 append해서 마지막에 삽입
        num_list.append(num_list.pop(0))

    print(f'#{tc} {num_list[0]}')