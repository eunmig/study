n = int(input())

arr = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    friend = 0
    for j in range(n):
        # 
        if i == j:
            continue