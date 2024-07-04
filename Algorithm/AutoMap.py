# 점화식
# f(0) = 4 = 2**2
# f(1) = 9 = 3**2
# f(2) = 25 = 5**2
# => 한변에 존재하는 점의 개수의 제곱

import sys

n = int(input())

# 저장 테이블
dp = [0] * 16

# 초기화
dp[0] = 2

for i in range(1, n+1):
    dp[i] = dp[i-1] + (2**(i-1))

print(dp[n]**2)