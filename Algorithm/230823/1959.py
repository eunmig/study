import sys
sys.stdin = open('1959.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))

    # N, M의 순서가 바뀌게 되면 ai, bi도 순서가 바껴야함
    if N > M:
        N, M = M, N
        ai, bi = bi, ai

    # 합계를 담을 리스트 생성
    max_sum = []

    # 길이 맞춰 순회
    for i in range(M-N+1):
        result = 0
        # 짧은 길이에 맞춰 순회
        for j in range(N):
            result += ai[j] * bi[j+i]

        max_sum.append(result)

    print(f'#{tc}', max(max_sum))