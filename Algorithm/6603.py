import sys
input = sys.stdin.readline

# 백트레킹
# 오름차순으로 나열되있음

def lotto(arr, s, index, cnt):
    # 숫자가 6개면 그대로 출력
    if cnt == 6:
        print(*arr)
        return

    for i in range(index, len(s)):
        # s의 첫번째 arr에 지정
        arr[cnt] = s[i]
        # 재귀 호출
        lotto(arr, s, i+1, cnt+1)

while True:
    s = list(map(int, input().split()))

    if s[0] == 0:
        break

    # 6자리 리스트 생성 
    arr = [0] * 6

    lotto(arr, s[1:], 0, 0)
    print()