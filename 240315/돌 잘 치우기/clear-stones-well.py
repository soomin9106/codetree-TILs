from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

temp = [row[:] for row in arr] # 값을 계속 바꿀꺼니까!!

points = []
for _ in range(k):
    r, c = map(int, input().split())
    points.append((r -1, c - 1))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

visited= [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y]:
        return False
    
    if temp[x][y] == 1:
        return False
    
    return True

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))


def move():
    for point in points:
        x, y = point
        visited[x][y] = True
        bfs(x, y)

    cnt =0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    return cnt

removed_list = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            removed_list.append((i, j))

removed_combi = list(combinations(removed_list, m))

res = -int(1e9)
for remove in removed_combi:
    temp = [row[:] for row in arr] # 깊은 복사
    visited= [[False] * n for _ in range(n)]

    for r in remove:
        temp[r[0]][r[1]] = 0
    
    # print(temp)
    val = move()

    res = max(res, val)
    

print(res)