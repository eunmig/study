import sys
sys.stdin = open('10163.txt')

arr = [[0]*101 for _ in range(101)]
N = int(input())
for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for row in range(x, x+w):
        for col in range(y, y+h):
            # 빈격자 리스트에 각 색종이의 면적마다 다른 숫자를 채움
            # 입력받은 순서대로 면적에 각자 다른 숫자로 카운트되고
            # 입력받은 순서대로 자신의 넓이에 덮어씌워짐
            # 보이는 면적 = 전체 면적 - 겹쳐진 면적
            arr[row][col] = i+1

# 테스트 케이스만큼 돌면서 각 색종이 면적 출력
for i in range(1, N+1):
    count = 0
    for x in arr:
        count += x.count(i+1)
    print(count)