from collections import deque

n, k, u, d = map(int, input().split())

maps = [
    list(map(int, input().split()))
    for _ in range(n)
]

points = [
    (x, y)
    for x in range(n)
    for y in range(n)
]

# print('points', points)

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, val):
    return in_range(x, y) and \
            not visited[x][y] and \
            u <= abs(maps[x][y] - val) <= d

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def bfs():
    bfs_q = deque()
    for (x, y) in selected_points:
        visited[x][y] = True 
        bfs_q.append((x, y))

    while bfs_q:
        curx, cury = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curx + dx, cury + dy

            if can_go(nx, ny, maps[curx][cury]):
                visited[nx][ny] = True
                bfs_q.append((nx, ny))

def calc():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    return cnt

selected_points = []
ans = -1
def choose_points(idx):
    global ans
    if len(selected_points) == k:
        initialize_visited()
        bfs()
        count = calc()
        # print('coount', count)
        ans = max(ans, count)
        return 

    if idx >= len(points):
        return 

    choose_points(idx + 1)

    selected_points.append(points[idx])
    choose_points(idx + 1)
    selected_points.pop()


choose_points(0)
print(ans)