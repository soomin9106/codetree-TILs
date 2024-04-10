n, m, t = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

glasses = [[0] * n for _ in range(n)]

next_glasses = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    glasses[x-1][y-1] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 상하좌우 순서
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def move_glasses(x, y):
    max_val = 0
    max_x, max_y = -1, -1
    for dx, dy in zip(dxs, dys):

        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and arr[nx][ny] > max_val:
            max_val = arr[nx][ny]
            max_x, max_y = nx, ny

    return max_x, max_y

def initialize_next_glasses():
    for i in range(n):
        for j in range(n):
            next_glasses[i][j] = 0

def simulate():
    initialize_next_glasses()

    for i in range(n):
        for j in range(n):
            # 구슬이 있는 경우
            if glasses[i][j] == 1:
                curx, cury = move_glasses(i, j)
                next_glasses[curx][cury] += 1

    
    for i in range(n):
        for j in range(n):
            glasses[i][j] = next_glasses[i][j]

    for i in range(n):
        for j in range(n):
            if glasses[i][j] >= 2:
                glasses[i][j] = 0

def count():
    cnt = 0

    for i in range(n):
        for j in range(n):
            if glasses[i][j] == 1:
                cnt += 1

    return cnt 

ans = 0
for _ in range(t):
    simulate()

    ans = count()

print(ans)