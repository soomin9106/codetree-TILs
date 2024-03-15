from collections import deque

n, k = map(int, input().split())
arr = []

visited = [[False] * n for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

points = []
for _ in range(k):
    r, c = map(int, input().split())
    points.append((r - 1, c - 1))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y]:
        return False

    if arr[x][y] == 1:
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


for point in points:
    x, y = point
    visited[x][y] = True
    bfs(x, y)

cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            cnt += 1
# print(visited)
print(cnt)