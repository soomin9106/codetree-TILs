n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# → ↗ ↑ ↖ ← ↙ ↓ ↘
dxs = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dys = [0, 1, 1, 0, -1, -1, -1, 0, 1]

commands = []
for _ in range(m):
    d, p = map(int, input().split())
    commands.append((d, p))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

nutritions = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
def move_nutritions(d, p):
    global nutritions
    for idx, (x, y) in enumerate(nutritions):
        curx, cury = x, y
        for _ in range(p):
            nx, ny = curx + dxs[d], cury + dys[d]

            if nx >= n:
                nx = 0
            if ny >= n:
                ny = 0
            if nx < 0:
                nx = n - 1
            if ny < 0:
                ny = n - 1

            curx, cury = nx, ny
        nutritions[idx] = (curx, cury)

# 특수 영양제가 있는 땅의 리브로수는 높이가 1만큼 증가하고 대각선으로 인접한 높이 1 이상의 리브로수의 개수 만큼 높이가 증가
def grow():
    tri_xs = [-1, -1, 1, 1]
    tri_ys = [1, -1, 1, -1]

    for (x, y) in nutritions:
        maps[x][y] += 1

    for (x, y) in nutritions:
        cnt = 0
        # maps[x][y] += 1
        for dx, dy in zip(tri_xs, tri_ys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny):
                if maps[nx][ny] >= 1:
                    cnt += 1

        maps[x][y] += cnt

    # print('after grow', maps)

# 해당 년도에 특수 영양제를 맞은 땅을 제외하고 높이가 2 이상인 리브로수를 높이 2만큼 잘라내고 해당 땅 위에 특수 영양제
def adapt():
    global nutritions
    new_nutritions = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in nutritions and maps[i][j] >= 2:
                maps[i][j] -= 2
                new_nutritions.append((i, j))

    nutritions = new_nutritions

    # print('after adapt', maps)
    # print('nutritions', nutritions)

def calc():
    val = 0
    for i in range(n):
        for j in range(n):
            val += maps[i][j]

    return val

for d, p in commands:
    move_nutritions(d, p)

    grow()

    adapt()

ans = calc()
print(ans)