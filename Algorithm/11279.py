# 최대 힙
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
            # pop 할떄 다시 부호 바꿔줘서 출력
            # 최대 힙과 동일하게 출력 가능
            print(-heapq.heappop(q))
    # 부호를 변경해서 최소 힙에 넣어주기
    else:
        heapq.heappush(q, -x)