arr = input()       # 문자열 입력받기
subset = set()      # 중복되지않는 부분 문자열 저장

for i in range(len(arr)):
    for j in range(i, len(arr)):
        # arr의 i부터 j까지 부분 문자열
        temp = arr[i:j+1]
        subset.add(temp)
print(len(subset))