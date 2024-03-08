import sys 

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        
        subarray = arr[i: j + 1]
        avg = sum(subarray) / len(subarray)  # 부동소수점 나눗셈 사용
        avg_rounded = round(avg)  # 반올림하여 정수 값 비교
        # print(arr[i: j+ 1], avg)
        if avg in arr[i: j + 1]:
            cnt += 1

print(cnt)