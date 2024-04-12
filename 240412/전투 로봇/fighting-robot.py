from collections import deque 


n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 전역 변수
ans = 0
level_cnt = 0
visited = [[False] * n for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

# range 관련 함수들
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y): # 현재 좌표 레벨까지 (빈좌표라면 0)
    return in_range(x, y) and \
            not visited[x][y] and \
            robot_level >= arr[x][y]


# 로봇 초기 위치 및 레벨 초기화
robot_level = 2
robot_x, robot_y = -1, -1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            robot_x, robot_y = i, j

# 몬스터 위치 관리 리스트 정의 및 초기화
monsters = []
for i in range(n):
    for j in range(n):
        if arr[i][j] >= 1:
            monsters.append((arr[i][j], i, j))

def get_distance(x, y):
    return abs(robot_x - x) + abs(robot_y - y)

def find_available_monster():
    candidates = []

    for (lv, i, j) in monsters:
        if lv < robot_level:
            candidates.append((get_distance(i, j), lv, i, j))

    candidates.sort()

    if len(candidates) == 0:
        return []
    return candidates[0]

# 로봇 위치에서 치워야 될 몬스터까지의 최소 거리 구하기
def bfs(monster_lv, monster_x, monster_y):
    global monsters, robot_x, robot_y, level_cnt, robot_level

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    q = deque()
    q.append((robot_x, robot_y, 0))
    arr[robot_x][robot_y] = 0
    visited[robot_x][robot_y] = True

    while q:
        curx, cury, curstep = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curx + dx, cury + dy

            if (nx, ny) == (monster_x, monster_y):
                monsters.remove((arr[nx][ny], nx, ny))
                arr[nx][ny] = 9
                robot_x, robot_y = nx, ny
                level_cnt += 1

                if level_cnt == robot_level:
                    level_cnt = 0
                    robot_level += 1

                return curstep + 1

            if can_go(nx, ny):
                q.append((nx, ny, curstep + 1))

    return -1

def simulate():
    global ans
    monster_point = find_available_monster()

    if monster_point == []:
        return False

    _, monster_lv, monster_x, monster_y = monster_point

    step = bfs(monster_lv, monster_x, monster_y)
    # print('step', step)

    if step == -1:
        return False

    ans += step

    return True

while True:
    if not simulate():
        break

    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end = ' ')
    #     print()

    # print()

print(ans)