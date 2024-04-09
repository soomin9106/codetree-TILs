from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def initialize_new_arr(chosen_walls):
    new_arr = [row[:] for row in arr]  # 기존 배열 복사
    for (x, y) in chosen_walls:
        new_arr[x][y] = 1
    return new_arr

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs_fire(new_arr):
    visited_bfs = [[False] * m for _ in range(n)]
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

    ans = 0
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 0 and not visited_bfs[i][j]:
                ans += 1
    
    return ans


ans = 0
def choose_walls(x_idx, y_idx, chosen_walls):
    global ans
    if len(chosen_walls) == 3:
        new_arr = initialize_new_arr(chosen_walls)
        val = bfs_fire(new_arr)
        ans = max(ans, val)
        return 

    for i in range(x_idx, n):
        y_start = y_idx if i == x_idx else 0
        for j in range(y_start, m):
            if arr[i][j] == 0:
                choose_walls(i, j + 1, chosen_walls + [(i, j)])

choose_walls(0, 0, [])
print(ans)