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

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y]:
        return False
    
    if arr[x][y] == 0:
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

visited[0][0] = True
bfs(0, 0)
print(1 if visited[n-1][m-1] else 0)