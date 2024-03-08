import sys

n, k = map(int, input().split())
arr = [''] * 10001
points_list = []

for _ in range(n):
    point, alpha = map(str, input().split())
    points_list.append(int(point))
    arr[int(point)] = alpha

points_list = sorted(points_list)

res = -int(1e9)



for idx in range(len(points_list) - k + 1):
    val = 0
    for i in range(points_list[idx], points_list[idx] + k + 1):
        if arr[i] == 'G':
            val += 1
        elif arr[i] == 'H':
            val += 2
        else:
            continue
        res = max(res, val)
        
print(res)