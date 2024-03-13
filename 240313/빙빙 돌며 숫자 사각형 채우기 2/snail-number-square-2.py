n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

dxs =[1, 0, -1, 0]
dys = [0, 1, 0, -1]
d = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

arr[0][0] = 1
x, y = 0, 0
for i in range(2, n * m + 1):
    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        x, y = nx, ny
        arr[x][y] = i
    else:
        d = (d + 1) % 4
        x, y = x + dxs[d], y + dys[d]
        arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()