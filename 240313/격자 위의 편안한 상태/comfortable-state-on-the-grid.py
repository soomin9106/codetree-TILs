n, m = map(int, input().split())

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

arrs = [[0] * n for _ in range(n)]


for _ in range(m):
    x, y = map(int, input().split())
    arrs[x - 1][y - 1] = 1
    x, y = x - 1, y - 1
    cnt = 0
    for k in range(4):
        nx, ny = x + dxs[k], y + dys[k]
        if in_range(nx, ny) and arrs[nx][ny] == 1:
            cnt += 1
            
    if cnt == 3:
        print(1)
    else:
        print(0)

# print(res)