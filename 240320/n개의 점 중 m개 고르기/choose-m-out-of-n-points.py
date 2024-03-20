import math

n, m = map(int, input().split())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))


selected_points = []
res = int(1e9)
distance = -int(1e9)
selecteds = []

def calc(cur_idx, cnt):
    global distance, selecteds
    if cnt == 2:
        # print(selecteds)
        x1, y1 = selecteds[0]
        x2, y2 = selecteds[1]
        distance = max(distance, (x1-x2)**2 + (y1-y2)**2)
        return

    if cur_idx == len(selected_points):
        return

    calc(cur_idx + 1, cnt)
    selecteds.append(selected_points[cur_idx])
    calc(cur_idx+1, cnt+1)
    selecteds.pop()

def dfs(cur_idx, cnt):
    global res, selected_points, distance
    if cnt == m:
        distance = -int(1e9)
        calc(0, 0)
        res = min(res, distance)
        return 
    
    if cur_idx == n:
        return

    dfs(cur_idx + 1, cnt)

    selected_points.append(points[cur_idx])
    dfs(cur_idx + 1, cnt +1)
    selected_points.pop()

dfs(0, 0)
print(res)