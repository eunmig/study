# 부분집합
def f(i, N):
    if i == N:
        print
        for j in range(N):
            if bit[j]:
                print(A[j], end=" ")
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

# 부분집합의 합_재귀
def f(i, N):
    if i == N:
        print(bit, end=" ")
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end=" ")
        print(f': {s}')
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        return

# 부분집합의 합_재귀2
def f(i, N, s):     # s: i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end=" ")
        print(f': {s}')
        return
    else:
        bit[i] = 1      # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i])
        bit[i] = 0      # 부분집합에 A[i] 미포함
        f(i+1, N, s)
        return

A = [1, 2, 3]
f(0, 3, 0)
bit = [0] * 3

