n, r, c = map(int, input().split())

r -= 1
c -= 1


arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


# 상하좌우 순서
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

cur = arr[r][c]
print(cur, end = ' ')

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

while True:
    flag = False
    for dx, dy in zip(dxs, dys):
        nr, nc = r + dx, c + dy 

        if in_range(nr, nc) and arr[nr][nc] > cur:
            print(arr[nr][nc], end = ' ')
            flag = True
            r, c= nr, nc
            cur = arr[nr][nc]
            break 

    if not flag:
        break