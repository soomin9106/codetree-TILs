import sys

n, k = map(int, input().split())
arr = [''] * 10001
points_list = []

for _ in range(n):
    point, alpha = map(str, input().split())
    points_list.append(int(point))
    arr[int(point)] = alpha

points_list.sort()

res = -int(1e9)

for point in points_list:
    if point + k in points_list:
        val = 0
        for i in range(point, point + k + 1):
            if arr[i] == 'G':
                val += 1
            elif arr[i] == 'H':
                val += 2
            else:
                continue
        res = max(res, val)
print(res)