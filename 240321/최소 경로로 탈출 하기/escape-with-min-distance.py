from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        cur_x, cur_y, cur_cost = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] != 0:
                arr[nx][ny] = cur_cost + 1
                q.append((nx, ny, cur_cost + 1))
                visited[nx][ny] = True

bfs(0, 0)
print(arr[n-1][m-1])