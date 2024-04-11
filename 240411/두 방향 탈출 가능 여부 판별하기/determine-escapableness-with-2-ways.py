n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

dxs = [1, 0]
dys = [0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            arr[x][y] == 1

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            dfs(nx, ny)

dfs(0, 0)

print(0 if not visited[n - 1][m - 1] else 1)