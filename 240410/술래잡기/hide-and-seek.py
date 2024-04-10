n, m, h, k = map(int, input().split())

hiders = [
    [[] for _ in range(n)]
    for _ in range(n)
]

next_hiders = [
    [[] for _ in range(n)]
    for _ in range(n)
]

tree = [
    [False] * n
    for _ in range(n)
]

seeker_next_dir = [
    [0] * n
    for _ in range(n)
]

seeker_rev_dir = [
    [0] * n
    for _ in range(n)
]

seeker_pos = (n // 2, n // 2)
forward_facing = True

ans = 0

for _ in range(m):
    x, y, d = map(int, input().split())
    hiders[x-1][y-1].append(d)

for _ in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True

def initialize_seeker_path():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    cur_x, cur_y = n // 2, n // 2
    move_dir, move_num = 0, 1

    while cur_x or cur_y:
        for _ in range(move_num):
            seeker_next_dir[cur_x][cur_y] = move_dir
            cur_x, cur_y = cur_x + dxs[move_dir], cur_y + dys[move_dir]
            seeker_rev_dir[cur_x][cur_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

            if not cur_x and not cur_y:
                break

        move_dir = (move_dir + 1) % 4
        if move_dir == 0 or move_dir == 2:
            move_num += 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def hider_move(x, y, move_dir):
    dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0]

    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    if not in_range(nx, ny):
        move_dir = 1 - move_dir if move_dir < 2 else 5 - move_dir
        nx, ny = x + dxs[move_dir], y + dys[move_dir]

    if (nx, ny) != seeker_pos:
        next_hiders[nx][ny].append(move_dir)
    else:
        next_hiders[x][y].append(move_dir)

def dist_from_seeker(x, y):
    seeker_x, seeker_y = seeker_pos
    return abs(seeker_x - x) + abs(seeker_y - y)

def hider_move_all():
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []

    for i in range(n):
        for j in range(n):
            if dist_from_seeker(i, j) <= 3:
                for move_dir in hiders[i][j]:
                    hider_move(i, j, move_dir)

            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)

    
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]

def get_seeker_dir():
    x, y = seeker_pos

    move_dir = 0

    if forward_facing:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]

    return move_dir

def check_facing():
    global forward_facing

    if seeker_pos == (0, 0) and forward_facing:
        forward_facing = False

    if seeker_pos == (n // 2, n // 2) and not forward_facing:
        forward_facing = True


def seeker_move():
    global seeker_pos

    x, y = seeker_pos

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    move_dir = get_seeker_dir()

    seeker_pos = (x + dxs[move_dir], y + dys[move_dir])

    check_facing()

def get_score(t):
    global ans 

    # 상우하좌 순서대로 넣어줍니다.
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 현재 술래의 위치를 불러옵니다.
    x, y = seeker_pos
    
    # 술래의 방향을 불러옵니다.
    move_dir = get_seeker_dir()

    # 3칸을 바라봅니다.
    for dist in range(3):
        nx, ny = x + dist * dxs[move_dir], y + dist * dys[move_dir]
        
        # 격자를 벗어나지 않으며 나무가 없는 위치라면 
        # 도망자들을 전부 잡게 됩니다.
        if in_range(nx, ny) and not tree[nx][ny]:
            # 해당 위치의 도망자 수 만큼 점수를 얻게 됩니다.
            ans += t * len(hiders[nx][ny])

            # 도망자들이 사라지게 됩니다.
            hiders[nx][ny] = []

def simulate(t):
    # 도망자가 움직입니다.
    hider_move_all()

    # 술래가 움직입니다.
    seeker_move()
    
    # 점수를 얻습니다.
    get_score(t)


# 술래잡기 시작 전에
# 구현상의 편의를 위해
# 술래 경로 정보를 미리 계산합니다.
initialize_seeker_path()

# k번에 걸쳐 술래잡기를 진행합니다.
for t in range(1, k + 1):
    simulate(t)

print(ans)