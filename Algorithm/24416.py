n = int(input())

cnt1, cnt2 = 0, 0

def fibo(n):
    global cnt1

    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

f = [0] * (n+1)     # DP 테이블 초기화
def fibonacci(n):
    f[1] = 1
    f[2] = 1
    global cnt2

    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        cnt2 += 1
    return f[n]

fibo(n)
fibonacci(n)
print(cnt1, cnt2)
