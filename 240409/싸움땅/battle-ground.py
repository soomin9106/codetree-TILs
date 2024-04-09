EMPTY = (-1, -1, -1, -1, -1, -1)
n, m, k = map(int, input().split())

# 각 칸마다 놓여있는 총 목록을 관리
gun = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j] != 0:
            gun[i][j].append(nums[j])

# 각 칸마다 플레이어 정보를 관리합니다.
# 순서대로 (num, x, y, d, s, a) 정보를 관리합니다.
# (x, y)위치에서 방향 d를 보고 있으며
# 초기 능력치가 s인 num번 플레이어가
# 공격력이 a인 총을 들고 있음을 뜻합니다.
# 총이 없으면 a는 0입니다.
players = []
for i in range(m):
    x, y, d, s = tuple(map(int, input().split()))
    players.append((i, x - 1, y - 1, d, s, 0))

# ↑, →, ↓, ←
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 플레이어들의 포인트 기록
points = [0] * m

# (x, y)가 격자를 벗어나는지 확인합니다.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 현재 (x, y)위치에서 방향 d를 보고 있을 때
# 그 다음 위치와 방향을 찾아줍니다.
def get_next(x, y, d):
    nx, ny = x + dxs[d], y + dys[d]

    if not in_range(nx, ny):
        d = (d + 2) % 4
        nx, ny = x + dxs[d], y + dys[d]

    return (nx, ny, d)

# 해당 칸에 있는 Player를 찾아줍니다.
# 없다면 EMPTY를 반환합니다.
def find_player(pos):
    for i in range(m):
        _, x, y, _, _, _ = players[i]

        if pos == (x, y):
            return players[i]

    return EMPTY

# Player p의 정보를 갱신해줍니다.
def update(p):
    num, _, _, _, _, _ = p

    for i in range(m):
        num_i, _, _, _, _, _ = players[i]

        if num == num_i:
            players[i] = p
            break

# 플레이어 p를 pos 위치로 이동시켜줍니다.
def move(p, pos):
    num, x, y, d, s, a = p
    nx, ny = pos

    gun[nx][ny].append(a)
    gun[nx][ny].sort(reverse=True)
    a = gun[nx][ny][0]
    gun[nx][ny].pop(0)

    p = (num, nx, ny, d, s, a)
    update(p)

# 진 사람의 움직임을 진행합니다.
# 결투에서 패배한 위치는 pos입니다.
def loser_move(p):
    num, x, y, d, s, a = p

    gun[x][y].append(a)

    for i in range(4):
        ndir = (d + i) % 4
        nx, ny = x + dxs[ndir], y + dys[ndir]

        if in_range(nx, ny) and find_player((nx, ny)) == EMPTY:
            p = (num, x, y, ndir, s, 0)
            move(p, (nx, ny))
            break

def duel(p1, p2, pos):
    num1, _, _, d1, s1, a1 = p1
    num2, _, _, d2, s2, a2 = p2

    if (s1 + a1, s1) > (s2 + a2, s2):
        points[num1] += (s1 + a1) - (s2 + a2)
        loser_move(p2)
        move(p1, pos)

    else:
        points[num2] += (s2 + a2) - (s1 + a1)
        loser_move(p1)
        move(p2, pos)


def simulate():
    for i in range(m):
        num, x, y, d, s, a = players[i]

        nx, ny, ndir = get_next(x, y, d)

        next_player = find_player((nx, ny))

        curr_player = (num, nx, ny, ndir, s, a)
        update(curr_player)

        if next_player == EMPTY:
            move(curr_player, (nx, ny))
        else:
            duel(curr_player, next_player, (nx, ny))

for i in range(k):
    simulate()

for point in points:
    print(point, end = ' ')