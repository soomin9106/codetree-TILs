import sys 

n = int(input())
arr = [0] + list(map(int, input().split()))

res = -int(1e9)
sum_of_nums = 0


for i in range(1, n+1):
    if sum_of_nums < 0:
        sum_of_nums = arr[i]

    else:
        sum_of_nums += arr[i]

    res = max(res, sum_of_nums)

print(res)