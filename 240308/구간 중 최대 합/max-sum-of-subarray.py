import sys 

n, k = map(int, input().split())
arr = list(map(int, input().split()))

res = -int(1e9)

for i in range(n - k + 1):
    val = sum(arr[i: i + k])

    res = max(res, val)

print(res)