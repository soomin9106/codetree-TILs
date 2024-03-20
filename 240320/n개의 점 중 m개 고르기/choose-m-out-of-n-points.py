import math

n, m = map(int, input().split())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))


selected_points = []
res = int(1e9)

def calc():
    x1, y1 = selected_points[0]
    x2, y2 = selected_points[1]
    distance = (x2 - x1)**2 + (y2 - y1)**2
    return int(distance)

def dfs(cur_idx, cnt):
    global res, selected_points
    if cnt == 2:
        res = min(res, calc())
        return 
    
    if cur_idx == n:
        return

    dfs(cur_idx + 1, cnt)

    selected_points.append(points[cur_idx])
    dfs(cur_idx + 1, cnt +1)
    selected_points.pop()

dfs(0, 0)
print(res)