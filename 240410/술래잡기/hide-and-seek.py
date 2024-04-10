n, m, h, k = map(int, input().split())

ans = 0

runners = []
for _ in range(m):
    x, y, d = map(int, input().split())
    cur_d = 1 if d == 1 else 3
    runners.append((x - 1, y - 1, d, cur_d))

trees = []
for _ in range(h):
    x, y = map(int, input().split())
    trees.append((x - 1 , y - 1))

# 술래 좌표 (x, y)
catcher = (n // 2, n // 2)
is_forward = True
catcher_next_dir = [
    [0] * n
    for _ in range(n)
]

catcher_reverse_next_dir = [
    [0] * n
    for _ in range(n)
]

# 좌우상하 순서
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 도망자의 도망치기
def run(x, y, d, cur_d):
    cur_x, cur_y = x, y
    nd = cur_d
    nx, ny = cur_x + dxs[cur_d], cur_y + dys[cur_d]
    cx, cy = catcher[0], catcher[1]

    # 다음칸이 격자가 벗어나지 않는 경우
    if in_range(nx, ny):
        # 움직이려는 칸에 술래가 있는 경우
        if (nx, ny) != (cx, cy):
            cur_x, cur_y = nx, ny
    else:
        if cur_d == 1:
            nd = 0
        elif cur_d == 0:
            nd = 1
        elif cur_d == 3:
            nd = 2
        else:
            nd = 3

        nx, ny = cur_x + dxs[nd], cur_y + dys[nd]

        if (nx, ny) != (cx, cy):
            cur_x, cur_y = nx, ny

    
    return cur_x, cur_y, nd # 이동한 위치와 방향 반환

# 모든 도망자 조건에 맞게 움직이기
def run_all():
    global runners

    for i in range(len(runners)):
        x, y, d, cur_d = runners[i]
        if get_distance(x, y, catcher[0], catcher[1]) <= 3:
            nx, ny, nd = run(x, y, d, cur_d)
            runners[i] = (nx, ny, d, nd)

    


# 술래의 경로 계산 (달팽이 모양)
def initialize_catcher_path():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    cur_x, cur_y = n // 2, n // 2
    move_dir, move_num = 0, 1

    for _ in range(move_num):
        catcher_next_dir[cur_x][cur_y] = move_dir
        cur_x, cur_y = cur_x + dxs[move_dir], cur_y + dys[move_dir]
        catcher_reverse_next_dir[cur_x][cur_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

        if not cur_x and not cur_y:
            break

        move_dir = (move_dir + 1) % 4
        if move_dir == 0 or move_dir == 2:
            move_num += 1

def get_catcher_dir():
    x, y = catcher

    move_dir = 0

    if is_forward:
        move_dir = catcher_next_dir[x][y]
    else:
        move_dir = catcher_reverse_next_dir[x][y]

    return move_dir

def check_facing():
    global is_forward

    if catcher == (0, 0) and is_forward:
        is_forward = False

    if catcher == (n // 2, n // 2) and not is_forward:
        is_forward = True

def catcher_move():
    global catcher

    x, y = catcher

    # 상우하좌 순서대로 넣어줍니다.
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    move_dir = get_catcher_dir()

    catcher = (x + dxs[move_dir], y + dys[move_dir])

    check_facing()

def find_catchers(x, y):
    global runners
    val = 0
    idxs = []
    for idx, (curx, cury, d, cur_d) in enumerate(runners):
        if (x, y) == (curx, cury):
            val += 1
            idxs.append(idx)

    for i in idxs:
        runners.pop(i)

    return val

def get_score(t):
    global ans

    # 상우하좌 순서대로 넣어줍니다.
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    x, y = catcher

    move_dir = get_catcher_dir()

    for dist in range(3):
        nx, ny = x + dist * dxs[move_dir], y + dist * dys[move_dir]
        if in_range(nx, ny) and (nx, ny) not in trees:
            val = find_catchers(nx, ny)
            ans += t * val

def simulate(t):
    run_all()

    catcher_move()

    get_score(t)

initialize_catcher_path()

for t in range(1, k + 1):
    simulate(t)

print(ans)