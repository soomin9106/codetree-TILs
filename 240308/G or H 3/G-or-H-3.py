import sys

n, k = map(int, input().split())
max_position = 0  # 최대 위치 변수 추가
arr = [''] * 10001
points_list = []

for _ in range(n):
    point, alpha = map(str, input().split())
    point = int(point)
    points_list.append(point)
    arr[point] = alpha
    max_position = max(max_position, point)

points_list = sorted(points_list)

res = -int(1e9)

for idx in range(len(points_list)):
    val = 0
    if points_list[idx] + k >= 10000:
        break
    for i in range(points_list[idx], points_list[idx] + k + 1):
        if arr[i] == 'G':
            val += 1
        elif arr[i] == 'H':
            val += 2
        else:
            continue
        res = max(res, val)

print(res)