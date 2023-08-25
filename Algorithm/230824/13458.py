import sys
sys.stdin = open('13458.txt')

N = int(input())
student = list(map(int, input().split()))
main, sub = map(int, input().split())

# 총감독관은 강의장에 무조건 1명씩 배치
result = N
for i in range(len(student)):
    # 총감독관이 감시할 수 있는 학생의 수를 제외하고 부감독관이 감시할 학생수 고려
    student[i] -= main
    # 시험장에 학생이 없을 경우도 생각해야함.
    if student[i] > 0:
        if student[i] % sub > 0:
            result += student[i] // sub + 1
        else:
            result += student[i] // sub

print(result)