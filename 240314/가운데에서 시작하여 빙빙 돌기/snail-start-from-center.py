n = int(input())
arrs = [[0] * n for _ in range(n)]

# 거꾸로 돌리는 순서대로
dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

arrs[n-1][n-1] = n * n
x, y = n-1, n-1
d = 0


for i in range(n * n - 1, 0, -1):
    nx, ny = x + dxs[d], y + dys[d]

    if in_range(nx, ny) and arrs[nx][ny] == 0:
        # print(nx, ny, i)
        x, y = nx, ny
        arrs[x][y] = i
    else:
        d = (d + 1) % 4
        x, y = x + dxs[d], y + dys[d]
        arrs[x][y] = i

for i in range(n):
    for j in range(n):
        print(arrs[i][j], end = ' ')
    print()