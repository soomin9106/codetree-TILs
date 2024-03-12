dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


n, m = map(int, input().split())
res_arr = [[0] * (m + 1) for _ in range(n + 1)]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = 0, 0
d = 0

res_arr[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dxs[d], y + dys[d]

    if not is_range(nx, ny) or res_arr[nx][ny] != 0:
        d = (d + 1) % 4

    x, y = x + dxs[d], y + dys[d]
    res_arr[x][y] = i


for i in range(n):
    for j in range(m):
        print(res_arr[i][j], end = ' ')
    print()