n, m = map(int, input().split())

# 북동남서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

x, y, d = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return maps[x][y] == 0 and not visited[x][y]

def simulate():
    global x, y, d

    visited[x][y] = True

    for _ in range(4):
        next_d = (d -1 + 4) % 4
        nx, ny = x + dxs[next_d], y + dys[next_d]

        if can_go(nx, ny):
            d = next_d
            x, y = nx, ny
            return True

        else:
            d = next_d

    back_x, back_y = x - dxs[d], y - dys[d]
    if maps[back_x][back_y] == 0:
        x, y = back_x, back_y
        return True
    else:
        return False

while True:
    moved = simulate()

    if not moved:
        break

ans = sum([
    1 
    for i in range(n)
    for j in range(m)
    if visited[i][j]
])

print(ans)