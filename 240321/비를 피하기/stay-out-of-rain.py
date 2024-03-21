from collections import deque

n, h, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

s_pos = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if arr[i][j] == 3
]
step = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and arr[x][y] != 1 and not visited[x][y]

q = deque()

def bfs():
    while q:
        cur_x, cur_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                step[nx][ny] = step[cur_x][cur_y] + 1

for x, y in s_pos:
    q.append((x, y))
    visited[x][y] = 0
    step[x][y] = 0

bfs()

for i in range(n):
    for j in range(n):
        if arr[i][j] != 2:
            print(0, end = ' ')
        else:
            if not visited[i][j]:
                print(-1, end = ' ')
            else:
                print(step[i][j], end = ' ')
    print()