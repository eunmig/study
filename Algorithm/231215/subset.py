def print_subset(bit, arr, n):
    total = 0                   # 부분집합의 합
    for i in range(n):
        if bit[i]:
            print(arr[i], end=' ')
            total += arr[i]
        print(bit, total)


arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i                  # 0번 원소
    for j in range(2):
        bit[1] = j              # 1번 원소
        for k in range(2):
            bit[2] = k          # 2번 원소
            for l in range(2):
                bit[3] = l      # 3번 원소
                print_subset(bit, arr, 4)


# -------------------------------------
arr = [1, 2, 3]

n = len(arr)

# 1<<n -> 2^n, 원소가 n개일 경우의 모든 부분집합의 수
for i in range(1<<n):
    for j in range(n):
        # i의 j번째 비트가 1인지 아닌지를 검사하여 부분집합 출력력
        if i & (1<<j):
           print(arr[j], end=", ")
    print()
print()