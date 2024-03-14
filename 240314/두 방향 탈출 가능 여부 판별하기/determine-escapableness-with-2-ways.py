# 아래와 위 방향
dxs = [1, 0]
dys = [0, 1]

n, m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny] == 1:
            dfs(nx, ny)

dfs(0, 0)
print(1 if visited[n - 1][m - 1] else 0)