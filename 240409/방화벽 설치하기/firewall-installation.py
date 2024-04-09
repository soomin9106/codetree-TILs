from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

new_arr = [[0] * m for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

# 불 2, 방화벽 1, 빈칸 0
visited = [[False] * m for _ in range(n)]
visited_bfs = [[False] * m for _ in range(n)]  # BFS 탐색을 위한 visited 배열

def initialize_new_arr(chosen_walls):
    for i in range(n):
        for j in range(m):
            new_arr[i][j] = arr[i][j]

    for (x, y) in chosen_walls:
        new_arr[x][y] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def calc(chosen_walls):
    initialize_new_arr(chosen_walls)
    
    bfs_q = deque()
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 2:
                bfs_q.append((i, j))
                visited_bfs[i][j] = True

    while bfs_q:
        curx, cury = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curx + dx, cury + dy

            if in_range(nx, ny) and new_arr[nx][ny] == 0 and not visited_bfs[nx][ny]:
                visited_bfs[nx][ny] = True
                bfs_q.append((nx, ny))

    val = 0

    for i in range(n):
        for j in range(m):
            if not visited_bfs[i][j] and new_arr[i][j] == 0:
                val += 1

    return val

ans = 0
def choose_walls(x_idx, y_idx, chosen_walls):
    global ans
    if len(chosen_walls) == 3:
        val = calc(chosen_walls)
        ans = max(ans, val)
        return 

    for i in range(x_idx, n):
        y_idx = y_idx if i == x_idx else 0
        for j in range(y_idx, m):
            if not visited[i][j] and arr[i][j] == 0:
                visited[i][j] = True
                choose_walls(i, j + 1, chosen_walls + [(i, j)])
                visited[i][j] = False

choose_walls(0, 0, [])
print(ans)