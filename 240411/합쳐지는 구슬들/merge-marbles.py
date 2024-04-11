n, m, t = map(int, input().split())

glasses = [
    [[] for _ in range(n)]
    for _ in range(n)
]

next_glasses = [
    [[] for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dir_mapper = {
    'U': 0,
    'D': 1,
    'R': 2,
    'L': 3
}

# UDRL 순서
dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

# 초기 구슬 정보 입력 받기 
for i in range(m):
    r, c, d, w = map(str, input().split())
    r = int(r)
    c = int(c)
    w = int(w)

    glasses[r-1][c-1].append((i, dir_mapper[d], w))

def initialize_next_glasses():
    for i in range(n):
        for j in range(n):
            next_glasses[i][j] = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 특정 좌표의 이동
def move(i, x, y, d, w):
    global next_glasses
    nx, ny = x + dxs[d], y + dys[d]
    nd = d

    if not in_range(nx, ny):
        nx, ny = x, y
        if d == 0:
            nd = 1
        if d == 1:
            nd = 0
        if d == 2:
            nd = 3
        else:
            nd = 2

    next_glasses[nx][ny].append((i, nd, w))

# 모든 좌표 이동 시뮬레이션
def move_all():
    for x in range(n):
        for y in range(n):
            if len(glasses[x][y]) == 1:
                i, d, w = glasses[x][y][0]
                move(i, x, y, d, w)

# 구슬 충돌
def collusion():
    global glasses, next_glasses
    for x in range(n):
        for y in range(n):
            # 같은 위치에 2개 이상의 구슬
            if len(next_glasses[x][y]) >= 2:
                max_w = 0
                max_d = 0
                idx = 0

                next_glasses[x][y].sort()

                for (i, curd, curw) in next_glasses[x][y]:
                    max_w += curw
                    if i > idx:
                        idx = i
                        max_d = curd

                next_glasses[x][y] = []
                next_glasses[x][y].append((idx, max_d, max_w))

    for x in range(n):
        for y in range(n):
            glasses[x][y] = next_glasses[x][y]

# 전체 턴 시뮬레이션
def simulate():
    
    initialize_next_glasses()

    move_all()

    collusion()
                

for _ in range(t):
    simulate()

    # print('glasses', glasses)
    # print()

cnt = 0
max_w = 0

for i in range(n):
    for j in range(n):
        if len(glasses[i][j]) >= 1:
            cnt += 1
            idx, curd, curw = glasses[i][j][0]

            if curw > max_w:
                max_w = curw

print(cnt, max_w)