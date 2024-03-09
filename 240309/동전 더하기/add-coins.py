import sys

n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse = True)

res = 0
for i in arr:
    res += (k // i)
    k %= i

    # print(res)

print(res)