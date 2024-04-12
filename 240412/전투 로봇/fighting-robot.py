from collections import deque 

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 전역 변수
ans = 0
level_cnt = 0
visited = [[False] * n for _ in range(n)]
step = [[0] * n for _ in range(n)]
bfs_q = deque()

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


def bfs():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    while bfs_q:
        curx, cury = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curx + dx, cury + dy

            if can_go(nx, ny):
                bfs_q.append((nx, ny))
                step[nx][ny] = step[curx][cury] + 1
                visited[nx][ny] = True

def update(best_pos, new_pos):
    if best_pos == (-1, -1):
        return True
    
    best_x, best_y = best_pos
    nx, ny = new_pos

    return (step[best_x][best_y], best_x, best_y) > \
            (step[nx][ny], nx, ny)

def move():
    global robot_level, level_cnt, robot_x, robot_y
    global ans

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    visited[robot_x][robot_y] = True
    step[robot_x][robot_y] = 0
    bfs_q.append((robot_x, robot_y))
    bfs()

    best_pos = (-1, -1)
    for i in range(n):
        for j in range(n):
            # bfs 를 했는데도 방문을 못했거나, 몬스터가 아니거나, 몬스터의 레벨이 같은 경우에는 잡아먹지는 못함
            if not visited[i][j] or not arr[i][j] or \
                arr[i][j] == robot_level:
                continue

            new_pos = (i, j)
            if update(best_pos, new_pos): 
                best_pos = new_pos

    if best_pos != (-1, -1):
        best_x, best_y = best_pos

        ans += step[best_x][best_y]
        arr[best_x][best_y] = 0
        robot_x, robot_y = best_x, best_y
        level_cnt += 1

        if level_cnt == robot_level:
            robot_level += 1
            level_cnt = 0

        return True
    else:
        return False

    


while True:
    moved = move()
    if not moved:
        break

    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end = ' ')
    #     print()

    # print()

print(ans)