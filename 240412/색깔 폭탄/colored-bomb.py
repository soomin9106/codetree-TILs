from collections import deque

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

next_grid = [
    [-2 for _ in range(n)]
    for _ in range(n)
]

def print_grid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end = ' ')
        print()
    print()

def initialize_next_grid():
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = -2

visited = [[False] * n for _ in range(n)]

# 빨간 폭탄 초기 위치 파악
red_bombs = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            red_bombs.append((i, j))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, color):
    return in_range(x, y) and \
            not visited[x][y] and \
            (grid[x][y] == color or grid[x][y] == 0)

all_points = []
max_len = 0
ans = 0 # 점수 기록

# 빨간 색 아닌 좌표에서 찾기 시작 - 이것만 해도 될 듯
def find_bombs(x, y):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
        
    bomb_q = deque()

    visited[x][y] = True
    bomb_q.append((x, y))
    
    while bomb_q:
        curx, cury = bomb_q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curx + dx, cury + dy

            if can_go(nx, ny, grid[x][y]):
                visited[nx][ny] = True 
                bomb_q.append((nx, ny))


def get_bundle(x, y):
    find_bombs(x, y)

    bomb_cnt, red_cnt = 0, 0
    standard = (-1, -1)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                continue
            bomb_cnt += 1

            if grid[i][j] == 0:
                red_cnt += 1

            elif (i, -j) > standard:
                standard = (i, -j)

    stdx, stdy = standard
    return (bomb_cnt, -red_cnt, stdx, stdy)

def find_best_bundle():
    best_bundle = (-1, -1, -1, -1)

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 1:
                bundle = get_bundle(i, j)
                if bundle > best_bundle:
                    best_bundle = bundle
    
    return best_bundle

def remove():
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                grid[i][j] = -2

def gravity():
    # global grid, next_grid
    initialize_next_grid()

    for j in range(n):
        last_idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] == -2:
                continue
            if grid[i][j] == -1:
                last_idx = i
            next_grid[last_idx][j] = grid[i][j]
            last_idx -= 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

def rotate():
    initialize_next_grid()

    for j in range(n - 1, -1, -1):
        for i in range(n):
            next_grid[n - 1 -j][i] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

def clean(x, y):
    find_bombs(x, y)

    remove()

    gravity()

def simulate():
    global ans

    best_bundle = find_best_bundle()
    bomb_cnt, _, x, y = best_bundle

    if best_bundle == (-1, -1, -1, -1) or bomb_cnt <= 1:
        return False

    ans += bomb_cnt * bomb_cnt
    clean(x, -y)

    rotate()

    gravity()

    return True

while True:
    flag = simulate()

    if not flag:
        break

print(ans)