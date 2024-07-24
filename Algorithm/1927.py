# 최소 힙
import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    x = int(input())

    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            # 가장 작은 값 삭제 후 반환
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, x)