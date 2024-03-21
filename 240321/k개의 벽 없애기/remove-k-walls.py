from collections import deque

n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

points = []
for _ in range(2):
    r1, c1 = map(int, input().split())

    points.append((r1 -1 , c1 -1))

walls = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            walls.append((i, j))

selected_wall = []
visited_wall = [False] * len(walls)
visited = [[False] * n for _ in range(n)]

dxs = [1,-1,0,0]
dys = [0,0,1,-1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[i][j]
    for sw in selected_wall:
        temp[sw[0]][sw[1]] = 0

    q = deque()
    q.append((x, y, 0))

    while q:
        cur_x, cur_y, cur_cost = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and not visited[nx][ny] and temp[nx][ny] == 0:
                q.append((nx, ny, cur_cost + 1))
                temp[nx][ny] = cur_cost + 1
                visited[nx][ny] = True
    
    return int(1e9) if temp[points[1][0]][points[1][1]] == 0 else temp[points[1][0]][points[1][1]]
        

res = int(1e9)
def dfs(cur_num):
    global selected_wall, res, visited
    if cur_num == k:
        # print(selected_wall)
        visited = [[False] * n for _ in range(n)]
        val = bfs(points[0][0], points[0][1])
        # 계산
        res = min(res, val)
        return

    for i in range(cur_num, len(walls)):
        if visited_wall[i]:
            continue
        
        visited_wall[i] = True
        selected_wall.append(walls[i])
        dfs(cur_num + 1)
        selected_wall.pop()
        visited_wall[i] = False

dfs(0)
if res == int(1e9):
    print(-1)
    exit(0)
print(res)