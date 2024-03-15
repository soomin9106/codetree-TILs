from collections import deque

n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

r, c = map(int, input().split())
r, c= r - 1, c - 1

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, val):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if arr[x][y] >= val:
        return False
    return True

def bfs(x, y):
    q = deque()
    possibles = []
    q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy
            
            if can_go(nx, ny, arr[x][y]):
                visited[nx][ny] = True
                q.append((nx, ny))
                possibles.append((arr[nx][ny], nx, ny))

    # print(len(possibles))
    if len(possibles) == 0:
        return (-1, -1)


    possibles = sorted(possibles, key = lambda x: (-x[0], x[1], x[2]))
    
    return (possibles[0][1], possibles[0][2])



idx = 0
min_x, min_y = r, c
res_x, res_y = r, c
while idx < k:
    visited = [[False] * n for _ in range(n)]
    # print(min_x, min_y)
    min_x, min_y = bfs(min_x, min_y)

    if min_x == -1 and min_y == -1:
        break
    else:
        res_x, res_y = min_x, min_y

    idx += 1

print(res_x + 1, res_y + 1)