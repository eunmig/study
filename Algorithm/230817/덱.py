from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q.popleft())  # pop이 더 빠르게 실행
print(q.popleft())
print(q.popleft())

