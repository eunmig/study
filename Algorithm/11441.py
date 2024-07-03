import sys
input = sys.stdin.readline

n = int(input())    # 수의 개수
arr = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    i, j = map(int, input().split())
    print(sum(arr[i-1:j]))




