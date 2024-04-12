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
    global visited
    bomb_q = deque()
    points = []

    visited[x][y] = True
    bomb_q.append((x, y))
    points.append((x, y))

    
    while bomb_q:
        curx, cury = bomb_q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curx + dx, cury + dy

            if can_go(nx, ny, grid[x][y]):
                visited[nx][ny] = True 
                points.append((nx, ny))
                bomb_q.append((nx, ny))

    points.sort()

    return points

def choose_one_bombs(candidates):
    red_cnts = []

    for idx, candidate in enumerate(candidates):
        cnt = 0
        for (x, y) in candidate:
            if (x, y) in red_bombs:
                cnt += 1

        red_cnts.append((cnt, idx))

    red_cnts.sort(key = lambda x: x[0])
    min_cnt = red_cnts[0][0]

    if len(red_cnts) == 1:
        return candidates[red_cnts[0][1]]

    if red_cnts[1][0] != min_cnt: # min_cnt 를 가지는 요소가 하나라면 바로 맨 첫번째꺼 리턴
        return candidates[red_cnts[0][1]]

    mid_points = []

    for idx, candidate in enumerate(candidates):
        for (x, y) in candidate:
            if (x, y) not in red_bombs:
                mid_points.append((x, y, idx))
                break

    
    mid_points.sort(key = lambda x: (-x[0], x[1]))

    # print(mid_points[2])
    cand_idx = mid_points[0][2]

    return candidates[cand_idx]


def choose_bombs():
    global max_len, ans, visited
    max_len = 0 # 초기화
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 1:
                
                visited = [[False] * n for _ in range(n)]
                cur_points = find_bombs(i, j)
                all_points.append(cur_points)

    if len(all_points) == 0: 
        return False

    for ap in all_points:
        max_len = max(max_len, len(ap))

    if max_len < 2:
        return False

    candidates = []
    for ap in all_points:
        
        if len(ap) == max_len and ap not in candidates:
            candidates.append(ap)

    # 행 크고, 열 작은 순서대로 sort
    new_cands = []
    for candidate in candidates:
        candidate.sort(key = lambda x: (-x[0], x[1]))
        new_cands.append(candidate)

    one_bomb = choose_one_bombs(new_cands)
    ans += len(one_bomb) * len(one_bomb)

    # 폭탄 터트리기
    for (x, y) in one_bomb:
        grid[x][y] = -2

    return True

def gravity():
    # global grid, next_grid
    initialize_next_grid()
    
    for c in range(n):
        next_idx = n - 1
        for r in range(n-1, -1, -1):
            if grid[r][c] >= 0: # 빨간 돌도 내려줘야 하는 대상임
                next_grid[next_idx][c] = grid[r][c]
                next_idx -= 1

            if grid[r][c] == -1:
                while next_idx > r:
                    next_grid[next_idx][c] = -2
                    next_idx -= 1

                next_grid[next_idx][c] = grid[r][c]
                next_idx -= 1

        while next_idx >= 0:
            next_grid[next_idx][c] = -2
            next_idx -= 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

def rotate():
    initialize_next_grid()

    for i in range(n):
        for j in range(n):
            next_grid[n - 1 -j][i] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

# 이게 한 turn

while True:
    if not choose_bombs():
        break
    gravity()
    rotate()
    gravity()

    # 다음 턴을 위해 초기화
    red_bombs = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                red_bombs.append((i, j))

    all_points = []


print(ans)