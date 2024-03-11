n = int(input())
m = 0
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr += [y] * x 
    m += x


arr.sort()
# print(arr, m)

res = -int(1e9)
for i in range(m // 2):
    val = arr[i] + arr[m - i -1]
    res = max(res, val)

print(res)