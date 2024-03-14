import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

temp = arr

k = 1
max_safe_zone = 0

visited = [[False] * m for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not visited[nx][ny] and temp[nx][ny] != 0:
            visited[nx][ny] = True
            dfs(nx, ny)
min_h = min(min(row) for row in arr)
max_h = max(max(row) for row in arr)
for temp_k in range(1, max_h + 1):
    temp = arr
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if temp[i][j] <= temp_k:
                temp[i][j] = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and temp[i][j] != 0:
                visited[i][j] = True
                cnt += 1
                dfs(i, j)

    if cnt > max_safe_zone:
        max_safe_zone = cnt
        k = temp_k
    
print(k, max_safe_zone)