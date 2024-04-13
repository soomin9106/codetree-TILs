from collections import deque

# 공격자 선정
# 공격자의 공격 - 레이저 공격, 포탄 공격
# 포탑 부서짐
# 포탑 정비

n, m, k = map(int, input().split())

grid = [
    [(0, 0) for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    col = list(map(int, input().split()))
    for j in range(m):
        grid[i][j] = (col[j], 0) # 공격력, 시간

handicap = n + m
cur_t = 1 # 시점 1부터 시작

ax, ay = -1, -1
vx, vy = -1, -1

visited = [[False] * m for _ in range(n)]
bfs_q = deque()
available_steps = []

def print_grid():
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end = ' ')
        print()

    print()

# 만약 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지됩니다.
# 부서지지 않는 포탑이 1개면 True 반환 - 중지
def is_over():
    cnt = 0
    for i in range(n):
        for j in range(n):
            power, recent = grid[i][j]

            if power >= 1:
                cnt += 1

    if cnt == 1:
        return True
    else:
        return False

# 공격자 선정 비교 기준: (공격력, 가장 최근에 공격한 시간, 행과 열의 합, 열 값)
def choose_attacker():
    global ax, ay
    # 비교를 위한 리스트 만들기
    attacker_info = []
    for i in range(n):
        for j in range(m):
            power, recent = grid[i][j]
            if power == 0:
                continue
            else:
                attacker_info.append((power, -recent, -1 * (i + j), -1 * j))

    attacker_info.sort()

    power = attacker_info[0][0]
    sum_xy = -1 * attacker_info[0][2]
    y = -1 * attacker_info[0][3]
    attack_x, attack_y = sum_xy - y, y

    grid[attack_x][attack_y] = (power + handicap, cur_t)
    ax, ay = attack_x, attack_y

# 공격 대상자 설정: (공격력, 가장 최근에 공격한 시간, 행과 열의 합, 열 값)
def choose_victim():
    global vx, vy
    victim_info = []

    for i in range(n):
        for j in range(m):
            power, recent = grid[i][j]
            if power == 0:
                continue
            else:
                victim_info.append((-1 * power, recent, (i + j), j))

    victim_info.sort()

    idx = 0
    for i, vi in enumerate(victim_info):
        summ = victim_info[i][2]
        vi_y = victim_info[i][3]

        vi_x = summ - vi_y

        if (vi_x, vi_y) != (ax, ay):
            idx = i
            break


    power = -1 * victim_info[idx][0]
    recent = victim_info[idx][1]
    sum_xy = victim_info[idx][2]
    victim_y = victim_info[idx][3]

    victim_x = sum_xy - victim_y

    # return power, recent, victim_x, victim_y

    vx, vy = victim_x, victim_y

def can_go(x, y):
    return not visited[x][y] and grid[x][y][0] != 0 

# 레이저 공격을 위한 bfs
def bfs():
    global available_steps

    # 우/하/좌/상
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while bfs_q:
        curx, cury, cursteps = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curx + dx, cury + dy
            cnx, cny = nx, ny
            if nx == -1:
                cnx = n - 1
            if nx == n:
                cnx = 0
            if ny == -1:
                cny = m -1
            if ny == m:
                cny = 0

            if can_go(cnx, cny):
                visited[cnx][cny] = True

                if (cnx, cny) == (vx, vy):
                    available_steps.append(cursteps + [(cnx, cny)])
                else:
                    bfs_q.append((cnx, cny, cursteps + [(cnx, cny)]))


# 공격 시도
def attack():
    global bfs_q, visited, step, available_steps
    # 레이저 공격
    available_steps = []
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
    bfs_q.append((ax, ay, [(ax, ay)]))
    visited[ax][ay] = True
    bfs()

    minus_a = grid[ax][ay][0] // 2
    chosen_step = []
    # print('available_steps', available_steps)
    if len(available_steps) >= 1:
        chosen_step = available_steps[0]

        # print('chosen', chosen_step)
        # print_grid()
        for (x, y) in chosen_step:
            if (x, y) == (ax, ay):
                continue
            elif (x, y) == (vx, vy):
                grid[x][y] = (max(grid[x][y][0] - grid[ax][ay][0], 0), grid[x][y][1])
                continue
            grid[x][y] = (max(grid[x][y][0] - minus_a, 0), grid[x][y][1])
    # 포탄 공격 진행
    else:
        chosen_step = [(vx, vy)]
        grid[vx][vy] = (max(grid[vx][vy][0] - grid[ax][ay][0], 0), grid[vx][vy][1])
        dxs = [-1, 1, 0, 0, -1, -1, 1, 1]
        dys = [0, 0, -1, 1, 1, -1, 1, -1]

        for dx, dy in zip(dxs, dys):
            nx, ny = vx + dx, vy + dy
            cnx, cny = nx, ny
            if nx == -1:
                cnx = n - 1
            if nx == n:
                cnx = 0
            if ny == -1:
                cny = m - 1
            if ny == m:
                cny = 0

            if (cnx, cny) != (ax, ay):
                chosen_step.append((cnx, cny))
                grid[cnx][cny] = (max(grid[cnx][cny][0] - minus_a, 0), grid[cnx][cny][1])
        

    # 포탑 재정비
    for i in range(n):
        for j in range(m):
            if (i, j) not in chosen_step and (i, j) != (ax, ay) and (i, j) != (vx, vy) and grid[i][j][0] != 0:
                grid[i][j] = (grid[i][j][0] + 1, grid[i][j][1])

    return None


for _ in range(k):
    if is_over():
        break
    choose_attacker()
    # print_grid()
    choose_victim()
    # print('ax, ay, vx, vy', ax, ay, vx, vy)
    attack()

    # print_grid()

    cur_t += 1


# print_grid()
ans = 0 
for i in range(n):
    for j in range(m):
        power, recent = grid[i][j]

        if power != 0 and power > ans:
            ans = power

print(ans)