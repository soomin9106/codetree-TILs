from collections import deque

n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

step = [[0] * n for _ in range(n)]

# 비어있던 칸은 그냥 -1 
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            step[i][j] = -1

# k 개의 초기 상한 귤 개수
rottens = deque()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            rottens.append((i, j))


dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and arr[x][y] == 1

def bfs():
    while rottens:
        cur_x, cur_y = rottens.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[cur_x][cur_y] + 1
                rottens.append((nx, ny))

bfs()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and step[i][j] == 0:
            print(-2, end = ' ')
        else:
            print(step[i][j], end = ' ')
    print()