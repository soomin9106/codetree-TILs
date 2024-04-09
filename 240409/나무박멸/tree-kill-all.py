from collections import deque

n, m, k, c= map(int, input().split())
cur_m = 0
ans = 0

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

herbicides = [[(0, 0)] * n for _ in range(n)]
trees = []

dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]

def debug():
    for i in range(n):
        for j in range(n):
            print(maps[i][j], end = ' ')
        print()
    print()

# 초기 나무들 위치
for i in range(n):
    for j in range(n):
        if maps[i][j] >= 1:
            trees.append((i, j))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 1. 나무의 성장
def grow():
    for (x, y) in trees:
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and maps[nx][ny] >= 1:
                maps[x][y] += 1

# 2. 번식 진행
def breed():
    check_points = []
    for (x, y) in trees:
        temp_check_points = []
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and (nx, ny) not in herbicides and maps[nx][ny] == 0:
                temp_check_points.append((x, y, nx, ny))

        check_points.append(temp_check_points)

    for points in check_points:
        for (ox, oy, nx, ny) in points:
            maps[nx][ny] += maps[ox][oy] // len(points)

# 제초제 뿌리기 (특정 나무가 있는 지점에) - 박멸할 수 있는 나무 개수, 그 당시 포인트들 반환
def spread(x, y):
    tri_dxs = [-1, -1, 1, 1]
    tri_dys = [1, -1, 1, -1]

    sum_val = maps[x][y]
    ps = []
    ps.append((x, y))

    for dx, dy in zip(tri_dxs, tri_dys):
        for i in range(1, k + 1):
            nx, ny = x + i * dx, y + i * dy

            if in_range(nx, ny) and maps[nx][ny] >= 0:
                sum_val += maps[nx][ny]
                ps.append((nx, ny))
            else:
                break 

    
    return sum_val, ps

def make_h(ps):
    for (i, j) in ps:
        maps[i][j] = -2 # 제초제 적용
        herbicides[i][j] = (1, cur_m) # 제초제가 있다, 몇년도에 만들어졌다 정보 저장

def spread_all():
    ans = -int(1e9)
    ps = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 1:
                val, new_ps = spread(i, j)

                if val > ans:
                    # print(val, new_ps)
                    ans = val
                    ps = new_ps

    make_h(ps)

    return ans


def simulate():
    global ans, trees
    grow()
    # debug()
    breed()
    # debug()
    ans += spread_all()

    # 모든 작업이 완료 된 이후 tree 위치 다시 채우기
    new_tree = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 1:
                new_tree.append((i, j))

    trees = new_tree

    # 시간 지난 제초제 지우기
    for i in range(n):
        for j in range(n):
            if herbicides[i][j][0] == 1:
                if abs(herbicides[i][j][1] - cur_m) >= c:
                    herbicides[i][j] = (0, 0)
                    maps[i][j] = 0


for i in range(m):
    cur_m = i

    simulate()


print(ans)