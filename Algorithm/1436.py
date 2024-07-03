n = int(input())

# 종말번호
theEndNumber = 666
# 종말번호 업데이트
count = 0

# 반복문 탈출할때까지 반복
while True:
    # 숫자안에 종말번호가 포함되어 있으면
    if '666' in str(theEndNumber):
        # 종말번호 카운트 +1
        count += 1
        # 카운트 번호가 입력값과 같다면
        if count == n:
            break
    # 종말번호 업데이트
    theEndNumber += 1

print(theEndNumber)
