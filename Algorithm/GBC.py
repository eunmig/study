# 브루트포스(완전탐색)
# 구간에 속도를 입력해놓고 테스트 속도와 비교

import sys

# n: 구간의 개수, m: 테스트 구간의 길이
n, m = map(int, input().split())

# 101개의 제한속도 구간 만들기
limit = [0] * 101
# 현재 구간 세팅
now = 1

# 제한속도 입력
for _ in range(n):
    section, speed = map(int, input().split())
    # 구간에 속도 입력
    for i in range(now, now+section):
        limit[i] = speed
    # 구간 옮겨서 재세팅
    now = now + section

# 최대로 벗어난 제한 속도 세팅
max_result = 0
# 테스트 현재구간 세팅
text_now = 1

# 테스트 제한속도 입력
for _ in range(m):
    text_section, text_speed = map(int, input().split())
    # 구간 속도 비교
    for i in range(text_now, text_now+text_section):
        max_result = max(max_result, text_speed-limit[i])
    # 구간 옮겨서 재세팅
    text_now = text_now + text_section

# 최대 과속 출력
print(max_result)