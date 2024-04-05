n = int(input())
x, y = map(int, input().split())

DIR_NUM = 4

x -= 1
y -= 1

maps = [['.'] * n for _ in range(n)]

for i in range(n):
    val = input()

    for j in range(n):
        maps[i][j] = val[j]

# visited
visited = [
    [
        [False for _ in range(DIR_NUM)]
        for _ in range(n)
    ]
    for _ in range(n)
]
elapsed_time = 0

# 시계 방향 회전
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

direction = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 해당 위치에 벽이 있는지 없는지 파악
def wall_exist(x, y):
    return in_range(x, y) and maps[x][y] == '#'

def simulate():
    global x, y, direction, elapsed_time

    if visited[x][y][direction]:
        print(-1)
        exit(0)
    
    visited[x][y][direction] = True
    nx, ny = x + dxs[direction], y + dys[direction]

    # Step1 - Case1
    if wall_exist(nx, ny):
        direction = (direction - 1 + DIR_NUM) % DIR_NUM

    # Step2 - Case1: 바로 앞이 격자 밖이라면 이동하여 탈출
    elif not in_range(nx, ny):
        x, y = nx, ny 
        elapsed_time += 1
    
    # Case2 & Case3
    else:
        rx, ry = nx + dxs[(direction + 1) % DIR_NUM], ny + dys[(direction + 1) % DIR_NUM]

        if wall_exist(rx, ry):
            x, y = nx, ny
            elapsed_time += 1
        else:
            x, y = rx, ry
            direction = (direction + 1) % DIR_NUM
            elapsed_time += 2


while in_range(x, y):
    simulate()

print(elapsed_time)