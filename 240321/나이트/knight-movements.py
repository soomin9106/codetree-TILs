from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# 8 가지 위치
dxs = [-2, -2, -1, -1, 1, 1, 2, 2]
dys = [-1, 1, -2, 2, -2, 2, -1, 1]

visited = [[False] * n for _ in range(n)]
arr = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x, y, 0))

    while q:
        cur_x, cur_y, cur_cost = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and not visited[nx][ny]:
                arr[nx][ny] = cur_cost + 1
                visited[nx][ny] = True
                q.append((nx, ny, cur_cost + 1))

bfs(r1, c1)
if arr[r2][c2] == 0:
    print(-1)
    exit(0)


print(arr[r2][c2])