import sys 

n = int(input())
arr = list(map(int, input().split()))

res = 0
start_idx = 0

for i in range(1, len(arr)):
    if sum(arr[start_idx: i + 1]) < 0:
        start_idx = i + 1
        res = 0
    else:
        res = sum(arr[start_idx: i + 1])

print(res)