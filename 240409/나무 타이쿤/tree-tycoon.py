n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

directions = []
for _ in range(m):
    directions.append(tuple(map(int, input().split())))

# 1~8 까지의 방향
dxs = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dys = [0, 1, 1, 0, -1, -1, -1, 0, 1]

# 초기 특수 영양제 위치
nutritions = [[0] * n for _ in range(n)]
for i in range(n - 2, n):
    for j in range(0, 2):
        nutritions[i][j] = 1
nutritions_pos = [(n-2, 0),(n-2, 1), (n-1,0), (n-1,1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_one_nutritions(x, y, d, p):
    for _ in range(p):
        nx, ny = x + dxs[d], y + dys[d]

        if nx < 0:
            nx = n - 1
        if ny < 0:
            ny = n - 1
        if nx >= n:
            nx = 0
        if ny >= n:
            ny = 0

        if in_range(nx, ny):
            x, y = nx, ny

    return x, y

def move_all_nutritions(d, p):
    for idx, (x, y) in enumerate(nutritions_pos):
        nx, ny = move_one_nutritions(x, y, d, p)
        nutritions_pos[idx] = (nx, ny)
        nutritions[x][y] = 0

    for idx, (x, y) in enumerate(nutritions_pos):
        nutritions[x][y] = 1

def grow():
    for idx, (x, y) in enumerate(nutritions_pos):
        maps[x][y] += 1
    
    # 각 점마다 대각선 4방향을 확인
    for idx, (x, y) in enumerate(nutritions_pos):
        if in_range(x - 1, y - 1) and maps[x - 1][y - 1] >= 1:
            maps[x][y] += 1
        if in_range(x - 1, y + 1) and maps[x - 1][y + 1] >= 1:
            maps[x][y] += 1
        if in_range(x + 1, y - 1) and maps[x + 1][y - 1] >= 1:
            maps[x][y] += 1
        if in_range(x + 1, y + 1) and maps[x + 1][y + 1] >= 1:
            maps[x][y] += 1

def clean():
    for i in range(n):
        for j in range(n):
            if (i, j) in nutritions_pos:
                nutritions_pos.remove((i, j))
            else:
                if maps[i][j] >= 2:
                    maps[i][j] -= 2
                    nutritions_pos.append((i, j))

def simulate(d, p):
    # 영양제 위치 옮기기
    move_all_nutritions(d, p)

    grow()

    clean()

def calc_sum():
    sum_val = 0

    for i in range(n):
        for j in range(n):
            sum_val += maps[i][j]

    return sum_val

ans = 0
for (d, p) in directions:
    simulate(d, p)
    ans = calc_sum()


print(ans)