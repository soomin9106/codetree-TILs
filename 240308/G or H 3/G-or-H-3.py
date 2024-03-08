import sys

n, k = map(int, input().split())
max_position = 0  # 최대 위치 변수 추가
arr = [''] * 10001
points_set = set()

for _ in range(n):
    point, alpha = map(str, input().split())
    point = int(point)
    points_set.add(point)
    arr[point] = alpha
    max_position = max(max_position, point)

points_list = sorted(list(points_set))  # set을 list로 변환하여 정렬

res = -int(1e9)

for idx in range(len(points_list)):
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